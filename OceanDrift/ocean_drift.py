import sys
from opendrift.models.oceandrift import OceanDrift
from opendrift.readers import reader_netCDF_CF_generic
from opendrift.readers import reader_global_landmask
from datetime import datetime, timedelta

def main():
    try:
        # Parse command line arguments
        if len(sys.argv) < 8:
            raise ValueError("Longitude, Latitude, Year, Month, Day, Hour, and Minute arguments are required.")

        lon = float(sys.argv[1])
        lat = float(sys.argv[2])
        year = int(sys.argv[3])
        month = int(sys.argv[4])
        day = int(sys.argv[5])
        hour = int(sys.argv[6])
        minute = int(sys.argv[7])

        # Initialize OceanDrift model
        ocean_model = OceanDrift()
        script_dir = os.path.dirname(os.path.abspath(__file__))

        reader_norkyst = reader_netCDF_CF_generic.Reader(
            'https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')

        ocean_model.add_reader(reader_norkyst)
        
        # Configure the model
        ocean_model.add_readers_from_file(os.path.join(script_dir, "data_sources.txt"))  
        
        reader_landmask = reader_global_landmask.Reader()
        ocean_model.env.add_reader(reader_landmask)

        # Set start time based on input arguments
        start_time = datetime(year, month, day, hour, minute, 0)
        
        # Configure and run the model
        ocean_model.seed_elements(lon=lon, lat=lat, number=100, radius=1000, time=start_time)
        ocean_model.run(end_time=start_time + timedelta(hours=1), time_step=900,
                        time_step_output=3600, outfile='opendrift.nc', export_variables=['density'])

        # Output file
        
        output_file_path = "C:/the-crossing/Source/crossing/Python/PythonScriptOutput.txt"

        with open(output_file_path, 'w') as f:
            f.write(str(ocean_model))
            f.write("\nModel run complete.")
        
        print("Model run complete.")
    except Exception as e:
        output_file_path = "C:/the-crossing/Source/crossing/Python/PythonScriptOutput.txt"

        with open(output_file_path, 'w') as f:
            f.write(f"An error occurred: {e}")
        
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
