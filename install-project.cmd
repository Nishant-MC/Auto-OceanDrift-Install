cd PythonScripts
owershell -command "& {Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Force}"
pip install virtualenv virtualenvwrapper-win
python -m virtualenv .
.\scripts\activate
pip install numpy psutil setuptools wheel
pip install opendrift
deactivate
