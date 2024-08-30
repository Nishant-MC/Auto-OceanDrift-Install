import sys
import threading
import tkinter as tk
from opendrift.models.oceandrift import OceanDrift
from opendrift.readers import reader_netCDF_CF_generic
from opendrift.readers import reader_global_landmask
from datetime import datetime, timedelta
import os

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

class DriftApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ocean Drift Application")
        self.master.geometry("600x400")
        self.status_label = tk.Label(master, text="Running the model...", font=('Helvetica', 14))
        self.status_label.pack(pady=20)

        self.output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "PythonScriptOutput.txt")
        sys.stdout = open(self.output_file_path, 'w')
        sys.stderr = sys.stdout

        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run_drift_model)
        self.thread.start()

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def run_drift_model(self):
        while not self.stop_event.is_set():
            try:
                script_dir = os.path.dirname(os.path.abspath(__file__))
                coordinate_file_path = os.path.join(script_dir, "CurrentCoordinate.txt")
                lon, lat = get_coordinates_from_file(coordinate_file_path)

                current_time = datetime.now()
                year, month, day, hour, minute = current_time.year, current_time.month, current_time.day, current_time.hour, current_time.minute

                ocean_model = OceanDrift()
                reader_norkyst = reader_netCDF_CF_generic.Reader('https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')
                ocean_model.add_reader(reader_norkyst)
                data_sources_file_path = os.path.join(script_dir, 'data_sources.txt')
                ocean_model.add_readers_from_file(data_sources_file_path)
                reader_landmask = reader_global_landmask.Reader()
                ocean_model.env.add_reader(reader_landmask)

                start_time = datetime(year, month, day, hour, minute, 0)
                ocean_model.seed_elements(lon=lon, lat=lat, number=100, radius=1000, time=start_time)
                ocean_model.run(end_time=start_time + timedelta(hours=1), time_step=900, time_step_output=3600, outfile='opendrift.nc', export_variables=['density'])

                completion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                completion_message = f"Model run complete at {completion_time}. Coordinates: Longitude {lon}, Latitude {lat}."
                print(completion_message)
                self.status_label.config(text=completion_message)
            except Exception as e:
                print(f"An error occurred: {e}")
                self.status_label.config(text=f"An error occurred: {e}")
            finally:
                sys.stdout.flush()

            self.stop_event.wait(1800)  # Run every 30 minute

    def on_closing(self):
        self.stop_event.set()
        if self.thread.is_alive():
            self.thread.join()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DriftApp(root)
    root.mainloop()
