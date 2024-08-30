curl -L https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe -o python-3.12.5-amd64.exe
.\python-3.12.5-amd64.exe /quiet InstallAllUsers=1 InstallLauncherAllUsers=1 PrependPath=1 Include_test=0
del "python-3.12.5-amd64.exe"
