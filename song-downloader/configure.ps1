# Create a virutal environment
echo "Creating virtual env..."
python -m venv venv

.\venv\Scripts\activate

# installing project dependencies
echo "Installing project requirements...."
pip install -r requirements.txt
