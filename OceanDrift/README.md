# OceanDrift - Starter's Guide 


## Setting Up & Testing VENV


1. Install the Python virtualenv package and its wrapper for Windows

```
pip install virtualenv virtualenvwrapper-win
```

2. Navigate to your project path and create a clean virtual environment

```
python -m virtualenv .
```

3. Make sure you have the privileges required to run and set up your environment

First, make sure you're running your PowerShell instance as an administrator.

To toggle venv permissions on: 
```
Set-ExecutionPolicy RemoteSigned
```

Then type:
```
.\scripts\activate
```  

Check that your venv.cfg file has been created and that you are, in fact, inside your venv. `(PROJECT FOLDER NAME)` will appear before the PowerShell path if everything is all good.

To toggle venv permissions off: 
```
Set-ExecutionPolicy Restricted
```

To leave your virtual environment, type:
```
deactivate
```


# Running OceanDrift

4. Once inside your virtual environment, install the modules: numpy, psutil, setuptools, wheel.

```
pip install numpy psutil setuptools wheel
```

5. Find & then install GDAL using the CORRECT .whl file

NOTE: The correct wheel is version-dependent and changes depending on what distribution of Python your machine is running. If you're running something other than Python 3.12 on 64-bit Windows, the wheel file will differ from the one mentioned in the snippet below. Check the following link to see if there's an appropriate wheel. Download it and place it in your project directory - https://github.com/cgohlke/geospatial-wheels/releases

```
pip install .\GDAL-3.8.4-cp312-cp312-win_amd64.whl
```

6. You're ready to run the program.

```
python drift_app.py
```



# Alternative Running Method

4. Navigate to your project directory and store that value in a variable.

```
$x = $pwd.Path
$x = $x.Replace("\","/")
```

5. Use this to replace the relevant part of requirements.txt

```
$y = gc -raw requirements.txt
echo $y.Replace("[REPLACE THIS WITH PWD OUTPUT]", $x) > updated-requirements.txt
```

6. Find the CORRECT version of GDAL as shown above & install all requirements at once. 

```
pip install -r updated-requirements.txt
```