pip install virtualenv virtualenvwrapper-win
python -m virtualenv .
Set-ExecutionPolicy RemoteSigned
.\PythonScripts\scripts\activate
pip install numpy psutil setuptools wheel
pip install opendrift
deactivate
