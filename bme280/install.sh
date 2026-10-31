echo "Installing python3-venv, creating virtual environment and installing python libraries from requirements.txt..."
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt