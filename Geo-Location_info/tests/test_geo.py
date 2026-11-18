# test_geo.py to test if scripts are working correctly
import pytest 
from pathlib import Path
from my_package.geo import distance_km, total_distance

script_dir = Path(__file__).resolve().parent.parent / "src" / "my_package"

file_path = script_dir / "lat_long.csv"

def test_same_location():
    assert distance_km(39.74, -104.99, 39.74, -104.99) == 0

def test_distance_about_5570():
    assert distance_km(40.7128, -74.0060, 51.5074, -0.1278) == pytest.approx(5570.22, abs=1)

def test_one_degree_eq():
    assert distance_km(0, 0, 0, 1) == pytest.approx(111.19, abs=0.1)

def test_if_equal_to_another():
    assert distance_km(40.7128, -74.0060, 51.5074, -0.1278) == pytest.approx(distance_km(
                                                        51.5074, -0.1278, 40.7128, -74.0060))

@pytest.mark.parametrize("lat1, lon1, lat2, lon2, expected_msg", [
    (91, 0, 12, 10, "latitude out of range:"),
    (12, 181, 0, 13, "longitude out of range:")
])
def test_lat_lon_too_high(lat1, lon1, lat2, lon2, expected_msg):
    with pytest.raises(ValueError) as excinfo:
        distance_km(lat1, lon1, lat2, lon2) 

    assert expected_msg in str(excinfo.value)

# ensuring no issue with the exact boundary values
def test_exact_boundaries():
    distance_km(90, 180, -90, -180)
    
def test_whole_csv():
    assert total_distance(file_path) == pytest.approx(73087.72, abs=1)