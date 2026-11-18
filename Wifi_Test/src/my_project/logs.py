# logs.py to check wifi logs
import csv
from pathlib import Path
# ensuring information is pulled from the correct place
script_dir = Path(__file__).resolve().parent

file_path = script_dir / "wifi_signals.csv"
# function to parse dataset and offer information
def disconnects_per_hour(path):
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        number_of_disconnects = {}
        disconnect = "DISCONNECTED"
        # iterating for number of disconnects and the hour it occurred. 

        for row in reader:
            hour = row["time"][0:2]
            status = row["event"]
            # checking for errors
            try:
                hour_num = int(hour)
                # custom error to clarify bad data in set
            except ValueError as err:
                raise ValueError(f"Unexpected value in dataset in time: {hour}.") from err

            if not 0 <= hour_num <= 23:
                raise ValueError(f"Hour outside of known hour range: {hour}")

            # verifies disconnection status          
            if disconnect in status:
                number_of_disconnects.setdefault(hour, 0)
                number_of_disconnects[hour] += 1

    return number_of_disconnects

if __name__ == "__main__":
    print(disconnects_per_hour(file_path))