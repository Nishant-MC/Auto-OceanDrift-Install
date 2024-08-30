Invoke-WebRequest -UseBasicParsing -Uri 'https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe' -OutFile python-3.12.5-amd64.exe
.\python-3.12.5-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
setx /M path "%path%;C:\Program Files\Python312"
$env:PATH =$env:PATH+";C:\Program Files\Python312"
python --version