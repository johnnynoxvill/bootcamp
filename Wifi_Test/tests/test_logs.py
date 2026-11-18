import pytest 
from pathlib import Path
from my_project.logs import disconnects_per_hour

script_dir = Path(__file__).resolve().parent.parent / "src" / "my_project"

file_path = script_dir / "wifi_signals.csv"
file_path_2 = script_dir / "wifi_signals_bad.csv"

def test_signals():
    assert disconnects_per_hour(file_path) == {
        "12": 2, "13": 4, "15": 2}

def test_bad_input():
    with pytest.raises(ValueError):
        disconnects_per_hour(file_path_2)
