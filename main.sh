#!/bin/bash
set -e

echo "Installing dependencies"
./DepInstall.sh

echo "Installing Mongo"
./MongoInstall.sh

echo "Running app in dev"
cd ../frontend/
npm run dev:electron

echo "Creating Folders"
cd ../backend/app/
mkdir temps/
cd Video/
mkdir videos/

echo "Complete