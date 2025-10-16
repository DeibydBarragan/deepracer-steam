import os
import re
import pypandoc
import time
from typing import List

# Carpeta base donde buscará los README.md
base_dir = r"C:\Users\Usuario\Documents\Universidad\STEAM\deepracer-steam"


def _strip_high_unicode(text: str) -> str:
    """Elimina caracteres fuera del BMP (incluye la mayoría de emojis).

    Esto evita errores de LaTeX con caracteres Unicode no soportados por pdflatex.
    """
    # Rangos U+10000..U+10FFFF (caracteres suplentes como emojis)
    try:
        return re.sub(r"[\U00010000-\U0010ffff]", "", text)
    except re.error:
        # En entornos donde la regex de Unicode extendido no está disponible,
        # fall back a eliminar manualmente por código ordinal.
        return ''.join(ch for ch in text if ord(ch) <= 0xFFFF)


def convert_md_to_pdf(md_path: str) -> None:
    pdf_path = os.path.splitext(md_path)[0] + ".pdf"
    try:
        with open(md_path, encoding="utf-8") as f:
            content = f.read()

        cleaned = _strip_high_unicode(content)
        
        # Obtener el directorio del archivo .md para resolver rutas relativas de imágenes
        md_dir = os.path.dirname(os.path.abspath(md_path))
        
        # Crear archivo temporal con header LaTeX para controlar posición de imágenes
        header_tex = os.path.join(md_dir, ".pandoc_header_temp.tex")
        with open(header_tex, "w", encoding="utf-8") as hf:
            hf.write(r"""
\usepackage{float}
\let\origfigure\figure
\let\endorigfigure\endfigure
\renewenvironment{figure}[1][2] {
    \expandafter\origfigure\expandafter[H]
} {
    \endorigfigure
}
""")

        try:
            pypandoc.convert_text(
                cleaned,
                "pdf",
                format="md",
                outputfile=pdf_path,
                extra_args=[
                    "--standalone", 
                    "--pdf-engine=xelatex",
                    f"--resource-path={md_dir}",
                    f"--include-in-header={header_tex}"
                ],
            )
            print(f"✅ Convertido: {pdf_path}")
        finally:
            # Limpiar archivo temporal
            if os.path.exists(header_tex):
                os.remove(header_tex)
                
    except Exception as e:
        print(f"❌ Error al convertir {md_path}: {e}")


def _format_seconds(seconds: float) -> str:
    seconds = int(seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}h {m}m {s}s"
    if m:
        return f"{m}m {s}s"
    return f"{s}s"


def _collect_md_files(base: str) -> List[str]:
    md_files: List[str] = []
    for root, _, files in os.walk(base):
        for file in files:
            if file.lower().endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files


def main() -> None:
    md_files = _collect_md_files(base_dir)
    total = len(md_files)
    if total == 0:
        print("No se encontraron archivos .md en:", base_dir)
        return

    start = time.perf_counter()
    # imprimir barra de progreso en una sola línea (sobrescribe la misma línea)
    bar_width = 40
    for idx, md_path in enumerate(md_files, start=1):
        file_start = time.perf_counter()
        convert_md_to_pdf(md_path)
        elapsed = time.perf_counter() - start
        avg = elapsed / idx
        remaining = avg * (total - idx)
        percent = idx / total
        filled = int(bar_width * percent)
        bar = '█' * filled + '-' * (bar_width - filled)
        percent_display = percent * 100
        short_name = os.path.basename(md_path)
        eta = _format_seconds(remaining)
        line = f"[{bar}] {idx}/{total} {percent_display:5.1f}% — {short_name} — ETA: {eta} — elapsed: {_format_seconds(elapsed)}"
        # \r para sobrescribir la línea; flush True para inmediata visualización
        print(line + "\r", end="", flush=True)

    # Finalizar con una nueva línea para no sobreescribir el prompt
    print()


if __name__ == "__main__":
    main()
