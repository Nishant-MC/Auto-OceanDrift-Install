import sys
import subprocess
import schedule
import time
from datetime import datetime
import os

def run_ocean_drift():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        coordinate_file_path = os.path.join(script_dir, "CurrentCoordinate.txt")
        lon, lat = get_coordinates_from_file(coordinate_file_path)
        now = datetime.utcnow()

        python_executable = sys.executable
        script_path = os.path.join(script_dir, "drift_app.py")
        command = [
            python_executable,
            script_path,
            str(lon),
            str(lat),
            str(now.year),
            str(now.month),
            str(now.day),
            str(now.hour),
            str(now.minute)
        ]

        result = subprocess.run(command, capture_output=True, text=True)
        output_file_path = os.path.join(script_dir, "PythonScriptOutput.txt")
        with open(output_file_path, 'a') as f:
            f.write(result.stdout)
            if result.stderr:
                f.write(result.stderr)
        
        print("Model run complete.")
    except Exception as e:
        output_file_path = os.path.join(script_dir, "PythonScriptOutput.txt")
        with open(output_file_path, 'a') as f:
            f.write(f"An error occurred: {e}\n")
        
        print(f"An error occurred: {e}", file=sys.stderr)

def get_coordinates_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lon_line = next(line for line in lines if line.startswith('Longitude'))
            lat_line = next(line for line in lines if line.startswith('Latitude'))
            lon = float(lon_line.split(':')[1].strip())
            lat = float(lat_line.split(':')[1].strip())
            return lon, lat
    except Exception as e:
        raise ValueError(f"Error reading coordinates from file: {e}")

schedule.every(30).minute.do(run_ocean_drift)

while True:
    schedule.run_pending()
    time.sleep(30)
