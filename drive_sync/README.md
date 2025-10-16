# Resumen

Este directorio contiene utilidades para sincronizar el repositorio local con la carpeta de Drive donde se guardan los avances del proyecto, y para convertir README/Markdown a PDF.

Archivos principales:

- `convert_readme.py`: recorre el repositorio buscando `.md` y convierte cada uno a `.pdf` (usa Pandoc + XeLaTeX). El script limpia emojis problemáticos y muestra una barra de progreso.
- `run_convert_readme.bat`: helper para ejecutar `convert_readme.py` en Windows.
- `sync_drive.bat`: sincroniza la carpeta local con la carpeta de Drive (mantiene los avances del proyecto) - versión Windows.
- `sync_drive.sh`: sincroniza la carpeta local con la carpeta de Drive (mantiene los avances del proyecto) - versión Linux/macOS.

Uso rápido:

Desde PowerShell en esta carpeta (Windows):

```powershell
.\run_convert_readme.bat   # convierte todos los .md a .pdf
.\sync_drive.bat    # sincroniza con la carpeta de Drive
```

Desde Bash en esta carpeta (Linux/macOS):

```bash
./sync_drive.sh    # sincroniza con la carpeta de Drive (asegúrate de dar permisos: chmod +x sync_drive.sh)
python3 convert_readme.py   # convierte todos los .md a .pdf
```

Requisitos (solo para `convert_readme.py`): Python, Pandoc y un motor LaTeX con XeLaTeX (MiKTeX o TeX Live). Instala `pypandoc` en el entorno Python.