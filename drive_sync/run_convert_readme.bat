@echo off
REM run_convert_readme.bat - Ejecuta convert_readme.py desde la carpeta del .bat
REM Cambia al directorio del .bat y ejecuta con python; en caso de error intenta "py -3"
setlocal
cd /d "%~dp0"
echo Ejecutando convert_readme.py desde %CD%

REM Intentar 'python'
python .\convert_readme.py %*
if %ERRORLEVEL% NEQ 0 (
    echo 'python' devolvio error %ERRORLEVEL%. Intentando 'py -3'...
    py -3 .\convert_readme.py %*
)
endlocal
n