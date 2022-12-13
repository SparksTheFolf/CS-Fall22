"""calculate the hotel_rates total from the hotels_rates.json file"""

from itertools import permutations, combinations_with_replacement
from json import load

with open("city_temp_dist.json") as file:  # load json structure representing a list of dictionaries
    cities = load(file)  # city list
with open("hotel_rates.json") as file:  # load json structure representing a dictionary
    hotel_rates = load(file)  # hotel dictionary


def hotel_costs(hotels: tuple) -> int:
    """Hotel cost total"""
    total = 0
    for hotel in hotels:
        total += hotel_rates[hotel]
    return total

print(hotel_costs(("Hilton")))