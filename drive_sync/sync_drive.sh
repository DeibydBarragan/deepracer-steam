#!/bin/bash
# ===============================================
# Sincroniza la carpeta local deepracer-steam con Google Drive
# usando rclone y la carpeta con ID especificado
# ===============================================

# Ruta donde está instalado rclone
RCLONE_PATH="rclone"

# Carpeta local a sincronizar
LOCAL_PATH="$HOME/Documents/Universidad/STEAM/deepracer-steam"

# Nombre del remoto configurado en rclone
REMOTE_NAME="deepracer-steam-drive"

# ID de la carpeta de destino en Google Drive
DRIVE_FOLDER_ID="15n3HbTbA0DiJlbOVLKdm9vE12lw_h27N"

# Ejecutar sincronización
echo "==============================================="
echo "Sincronizando archivos locales con Google Drive..."
echo "==============================================="
$RCLONE_PATH sync "$LOCAL_PATH" "${REMOTE_NAME}:" \
    --drive-root-folder-id "$DRIVE_FOLDER_ID" \
    --exclude ".git/**" \
    --exclude "LICENSE" \
    --exclude ".gitignore" \
    --exclude "drive_sync/**" \
    --progress

echo ""
echo "✅ Sincronización completada."
read -p "Presiona Enter para continuar..."
