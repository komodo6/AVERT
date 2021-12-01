import { app, BrowserWindow, nativeTheme } from "electron";
import { initialize, enable } from "@electron/remote/main";
import {PythonShell} from 'python-shell';
import path from "path";

let options = {
  scriptPath: '/usr/src/backend/',
};

let pyshell = new PythonShell('app.py', options);

initialize();

try {
  if (
    process.platform === "win32" &&
    nativeTheme.shouldUseDarkColors === true
  ) {
    require("fs").unlinkSync(
      require("path").join(app.getPath("userData"), "DevTools Extensions")
    );
  }
} catch (_) {}

let mainWindow;

pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});

function createWindow() {
  /**
   * Initial window options
   */
  mainWindow = new BrowserWindow({
    width: 1000,
    height: 600,
    minWidth: 1250,
    minHeight: 500,
    frame: false,
    useContentSize: true,
    webPreferences: {
      contextIsolation: true,

      // More info: /quasar-cli/developing-electron-apps/electron-preload-script
      preload: path.resolve(__dirname, process.env.QUASAR_ELECTRON_PRELOAD),
    },
  });

  enable(mainWindow.webContents);

  mainWindow.loadURL(process.env.APP_URL);

  mainWindow.setMenuBarVisibility(false);

  if (process.env.DEBUGGING) {
    // if on DEV or Production with debug enabled
    mainWindow.webContents.openDevTools();
  } else {
    // we're on production; no access to devtools pls
    mainWindow.webContents.on("devtools-opened", () => {
      mainWindow.webContents.closeDevTools();
    });
  }

  mainWindow.on("closed", () => {
    mainWindow = null;
  });
}

app.on("ready", createWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  if (mainWindow === null) {
    createWindow();
  }
});
