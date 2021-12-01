#!/bin/bash
set -e

sudo rm -r /usr/src/backend/

echo "Installing dependencies"
./DepInstall.sh

echo "Installing Mongo"
./MongoInstall.sh

echo "Installing Node"
./NodeInstall.sh

echo "Creating Folders"
cd ./backend/app/
mkdir temps/
cd Video/
mkdir videos/

echo "Build app"
cd ../../../
sudo cp -r backend/ /usr/src/
cd ./frontend/
source ~/.nvm/nvm.sh
npm install
npm run build:electron
ls -s ./dist/electron/avert-linux-x64/avert ~/Desktop/Avert

echo "Complete"