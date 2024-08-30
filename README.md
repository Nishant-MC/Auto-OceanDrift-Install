# Automated OceanDrift Setup

The goal is to get a simple and idiot-proof script to install the OceanDrift project and run it on a blank, 64-bit Windows machine without any hassles.


# Needed Subscripts

1. get-python (.cmd) - IN-PROGRESS, UNTESTED
   - Downloads and installs Python 3.12 onto the machine
   - Updates PATH env variable if required
   - Uses py launcher to get pip

2. download-project (.cmd) - DONE
   - Clones the git repo of the OceanDrift project
   - Grabs the relevant GDAL wheel from https://github.com/cgohlke/geospatial-wheels/releases
   - Packs it all together and does any required cleanup

3. install-project (.cmd)
   - Does the full OceanDrift README.md setup

4. run-project (.cmd)
   - Invokes .\activate
   - Runs drift_app
   - Invokes deactivate
  
# CURRENT PROGRESS: 1/4
