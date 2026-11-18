# geo.py: demo to study, not a lab answer
import math
import csv
from pathlib import Path

script_dir = Path(__file__).resolve().parent

file_path = script_dir / "lat_long.csv"

EARTH_RADIUS_KM = 6371.0

def distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Great-circle distance between two points (haversine formula)."""
    for lat in (lat1, lat2):
        if not -90 <= lat <= 90:
            raise ValueError(f"latitude out of range: {lat}")
    for lon in (lon1, lon2):
        if not -180 <= lon <= 180:
            raise ValueError(f"longitude out of range: {lon}")
        
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dlat = p2 - p1
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlon/ 2) ** 2
    return 2 * EARTH_RADIUS_KM * math.asin(math.sqrt(a))

def total_distance(path):
    with open(path, "r") as f:
        reader = csv.DictReader(f)

        prev_lat_lon = None
        current_lat_lon = None
        total_distance_travelled = 0

        for row in reader:
            current_lat_lon = list(map(float, [row["lat"], row["lon"]]))

            if prev_lat_lon is not None: 
                dist = distance_km(prev_lat_lon[0], prev_lat_lon[1], current_lat_lon[0], 
                                        current_lat_lon[1])
                total_distance_travelled += dist

            prev_lat_lon = current_lat_lon

        return total_distance_travelled

if __name__ == "__main__":
    print(f"The total distance traveled is {round(total_distance(file_path),2)}km")
