virtualenv --python=/usr/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$PWD/src