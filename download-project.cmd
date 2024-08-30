curl -L https://github.com/Nishant-MC/Auto-OceanDrift-Install/raw/main/PythonScripts.zip -o PythonScripts.zip
curl -L https://github.com/Nishant-MC/Auto-OceanDrift-Install/raw/main/install-project.cmd -o install-project.cmd
curl -L https://github.com/Nishant-MC/Auto-OceanDrift-Install/raw/main/run-project.cmd -o run-project.cmd
curl -L https://github.com/cgohlke/geospatial-wheels/releases/download/v2024.2.18/GDAL-3.8.4-cp312-cp312-win_amd64.whl -o GDAL-3.8.4-cp312-cp312-win_amd64.whl
tar -xf PythonScripts.zip
del "PythonScripts.zip"
move .\GDAL-3.8.4-cp312-cp312-win_amd64.whl .\PythonScripts\GDAL-3.8.4-cp312-cp312-win_amd64.whl
move .\install-project.cmd .\PythonScripts\install-project.cmd
move .\run-project.cmd .\PythonScripts\run-project.cmd
