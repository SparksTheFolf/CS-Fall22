"""
Author: Nolan T. (CS118 Fall Class)
Last Edited: 12/12/2022
Online Version Avail: https://github.com/SparksTheFolf/CS-Fall22

"""

from itertools import permutations, combinations_with_replacement
from json import load

HOTEL_BUDGET = 850

def avg_temp(route: tuple) -> float:
    """
    Calculating the average temp of a route
    :param route: list of cities
    :return: avg temp
    """
    pass


def hotel_costs(hotels: tuple) -> int:
    """
    Hotel cost total
    :param hotels: list of hotel names like:
    :return: sum of the per night cost
    """
    pass


def rte_to_str(route: tuple, closed: bool = False) -> str:
    """
    String representation of a route
    :param route: list of cities
    :param closed: True, means closing the loop, going back from the last location to to the start.
    :return: A string showing the intermediate points separated by '->'
    """
    pass


#
# only needed for bonus points
#

def rte_len(route: tuple, closed: bool = False) -> int:
    """
    Calculating the length of a route
    :param route: list of cities
    :param closed: True, means closing the loop, going back from the last location to to the start.
    :return: length of a closed route (i.e., returning to the start)
    """
    pass


with open("city_temp_dist.json") as file:  # load json structure representing a list of dictionaries
    cities = load(file)  # city list
with open("hotel_rates.json") as file:  # load json structure representing a dictionary
    hotel_rates = load(file)  # hotel dictionary

