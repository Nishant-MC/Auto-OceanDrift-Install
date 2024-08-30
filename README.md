# Automated OceanDrift Setup

The goal is to get a simple and idiot-proof script to install the OceanDrift project and run it on a blank, 64-bit Windows machine without any hassles.


# Needed Subscripts

1. get-python (.cmd) - DONE
   - Downloads and installs Python 3.12 onto the machine
   - Prepends Python folders to the PATH env variable
   - Cleans up the Python installer .exe

2. download-project (.cmd) - DONE
   - Downloads a .ZIP package of the OceanDrift project
   - Grabs the relevant GDAL wheel from https://github.com/cgohlke/geospatial-wheels/releases
   - Packs it all together and does any required cleanup

3. install-project (.cmd)
   - Does the full OceanDrift README.md setup

4. run-project (.cmd)
   - Invokes .\activate
   - Runs drift_app
   - Invokes deactivate
  
# CURRENT PROGRESS: 2/4
