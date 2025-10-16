@echo off
:: ===============================================
:: Sincroniza la carpeta local deepracer-steam con Google Drive
:: usando rclone y la carpeta con ID especificado
:: ===============================================

:: Ruta donde está instalado rclone
set RCLONE_PATH="C:\Program Files\rclone-v1.71.1-windows-amd64\rclone.exe"

:: Carpeta local a sincronizar
set LOCAL_PATH="C:\Users\Usuario\Documents\Universidad\STEAM\deepracer-steam"

:: Nombre del remoto configurado en rclone
set REMOTE_NAME=deepracer-steam-drive

:: ID de la carpeta de destino en Google Drive
set DRIVE_FOLDER_ID=15n3HbTbA0DiJlbOVLKdm9vE12lw_h27N

:: Ejecutar sincronización
echo ===============================================
echo Sincronizando archivos locales con Google Drive...
echo ===============================================
%RCLONE_PATH% sync %LOCAL_PATH% "%REMOTE_NAME%:" --drive-root-folder-id %DRIVE_FOLDER_ID% --exclude ".git/**" --exclude "LICENSE" --exclude ".gitignore" --progress

echo.
echo ✅ Sincronización completada.
pause
