"""
This is the first attempt at refreshing my Python skills!

"""

# Getting the math skills to easily parse information
import statistics
from collections import Counter

# Functions
# Gets the average reading
def average(readings):
	return round(statistics.mean(readings), 2)

# Gets the strongest reading (highest value)
def strongest(readings):
	return max(readings)

# Lists the usable networks
def usable(networks, threshold=-70):
	usable_networks = []

	for net in networks:
		if net["rssi"] > threshold:
			usable_networks.append(net["ssid"])

	return usable_networks

# Counts number of each word
def count_words(text: str) -> dict[str, int]:
	return dict(Counter(text.split()))


# Lists of data
wifi_readings = [-48, -80, -65]

all_networks = [
	{"ssid": "Home", "rssi": -48},
	{"ssid": "Work", "rssi": -80},
	{"ssid": "Coffee Shop", "rssi": -65}
]

wordy = "scan scan connect"

# Testing the functions
# print(average(wifi_readings))
# print(strongest(wifi_readings))
# print(usable(all_networks))
# print(count_words(wordy))

print(f"""The average reading is {average(wifi_readings)},
the strongest reading is {strongest(wifi_readings)},
the most usable wifi networks are {usable(all_networks)},
and the number of each of the words is {count_words(wordy)}.""")
	



