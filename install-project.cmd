pip install virtualenv virtualenvwrapper-win
python -m virtualenv .
Set-ExecutionPolicy RemoteSigned
.\scripts\activate
pip install numpy psutil setuptools wheel
pip install opendrift
deactivate
