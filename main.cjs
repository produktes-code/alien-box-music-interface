const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const http = require('http');

let mainWindow;
let backendProcess = null;

function startBackend() {
    const isPackaged = app.isPackaged;
    const baseDir = isPackaged ? process.resourcesPath : __dirname;
    
    // In dev we run the python script, in prod we run the PyInstaller exe
    const backendExecutableName = process.platform === 'win32' ? 'AlienBox.exe' : 'AlienBox';
    
    // The PyInstaller binary will be placed inside extraResources backend/ directory
    const backendPath = isPackaged 
        ? path.join(baseDir, 'backend', 'AlienBox', backendExecutableName)
        : 'python'; 
        
    const backendArgs = isPackaged ? [] : ['alienbox_server.py'];
    const cwd = isPackaged ? path.join(baseDir, 'backend', 'AlienBox') : __dirname;

    console.log(`Starting AlienBox backend from: ${backendPath} with cwd: ${cwd}`);
    
    backendProcess = spawn(backendPath, backendArgs, {
        cwd: cwd
    });

    backendProcess.stdout.on('data', (data) => {
        console.log(`[AlienBox stdout]: ${data}`);
    });

    backendProcess.stderr.on('data', (data) => {
        console.error(`[AlienBox stderr]: ${data}`);
    });

    backendProcess.on('close', (code) => {
        console.log(`AlienBox process exited with code ${code}`);
    });

    backendProcess.on('error', (err) => {
        console.error(`[AlienBox spawn error]: ${err.message}`);
        const { dialog } = require('electron');
        dialog.showErrorBox('AlienBox Server Error', `Failed to start server: ${err.message}`);
    });
}

function waitForServer(url, callback) {
    const checkServer = () => {
        http.get(url, (res) => {
            if (res.statusCode === 200 || res.statusCode === 404) {
                callback();
            } else {
                setTimeout(checkServer, 1000);
            }
        }).on('error', () => {
            setTimeout(checkServer, 1000);
        });
    };
    checkServer();
}

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1440,
        height: 900,
        backgroundColor: '#0a0a0a',
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true
        },
        title: 'Alien Box',
    });

    // We load the file directly from the filesystem or via the localhost server
    // Since alienbox_server.py also acts as an HTTP Server, we can load it through the server!
    const isPackaged = app.isPackaged;
    const baseDir = isPackaged ? process.resourcesPath : __dirname;
    
    // Wait for python server to be up
    waitForServer('http://localhost:8000', () => {
        // The server serves from its CWD. In packaged mode, CWD is process.resourcesPath/backend/AlienBox
        // But the frontend is in process.resourcesPath/splash_screen_organic_v3_final
        // To be safe, we just load the HTML file directly via file:// protocol.
        const htmlPath = path.join(baseDir, 'splash_screen_organic_v3_final', 'manual_multilingual_v14.html');
        mainWindow.loadURL(`file://${htmlPath}`);
    });

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

app.whenReady().then(() => {
    startBackend();
    createWindow();
});

app.on('will-quit', () => {
    if (backendProcess) {
        console.log('Terminating AlienBox backend...');
        backendProcess.kill();
    }
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (mainWindow === null) {
        createWindow();
    }
});
