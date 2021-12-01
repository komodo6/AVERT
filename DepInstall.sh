set -e

echo "Installing binaries"
sudo apt-get update
sudo apt-get install -y libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 ffmpeg

echo "Installing python packages"
pip3 install -r requirements.txt

echo "Complete"