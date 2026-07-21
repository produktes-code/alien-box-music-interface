@echo off
echo 👽 Building Alien Box for Windows (Portable Release) 👽

echo Cleaning previous builds...
rmdir /s /q dist_win
mkdir dist_win\AlienBox
mkdir dist_win\AlienBox\Frontend

echo Copying Backend...
copy alienbox_server.py dist_win\AlienBox\

echo Copying Frontend...
xcopy splash_screen_organic_v3_final\* dist_win\AlienBox\Frontend\ /s /e

echo Copying Manual...
copy AlienBox_Manual_Definitivo_Universal_V14.pdf dist_win\AlienBox\

echo Packaging ZIP Archive for Windows...
powershell Compress-Archive -Path dist_win\AlienBox -DestinationPath AlienBox_Windows_Portable.zip -Force

echo Build complete. Output: AlienBox_Windows_Portable.zip
