#!/bin/bash
echo "👽 Building Alien Box for macOS (.dmg) 👽"

# Limpiar build anterior
rm -rf build dist AlienBox.dmg

echo "Initializing PyInstaller..."
# Construir el binario de mac
python3 -m PyInstaller --name "AlienBox" --windowed alienbox_server.py

echo "Empaquetando Frontend y Manual en el .app..."
mkdir -p dist/AlienBox.app/Contents/Resources/Frontend
cp -r splash_screen_organic_v3_final/* dist/AlienBox.app/Contents/Resources/Frontend/
cp AlienBox_Manual_Universal.pdf dist/AlienBox.app/Contents/Resources/

echo "Creating DMG..."
hdiutil create -volname "Alien Box" -srcfolder dist/AlienBox.app -ov -format UDZO AlienBox_macOS_Installer.dmg

echo "Build complete. Output: AlienBox_macOS_Installer.dmg"
