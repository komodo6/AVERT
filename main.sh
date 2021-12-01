set -e

echo "Installing dependencies"
./DepInstall.sh

echo "Installing Mongo"
./MongoInstall.sh

echo "Running app in dev"
cd ../frontend
npm run dev:electron

echo "Complete