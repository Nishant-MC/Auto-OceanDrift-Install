powershell -command "& {Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Force}"
pip install virtualenv virtualenvwrapper-win
python -m virtualenv .
.\scripts\activate
pip install numpy psutil setuptools wheel
pip install .\GDAL-3.8.4-cp312-cp312-win_amd64.whl
pip install opendrift
deactivate
