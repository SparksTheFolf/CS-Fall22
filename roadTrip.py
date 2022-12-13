"""
Author: Nolan T. (CS118 Fall Class)
Last Edited: 12/12/2022
Online Version Avail: https://github.com/SparksTheFolf/CS-Fall22
This program is a road trip planner. It will take a list of cities and their temperatures and a list of hotels and their prices and will find the best route to take. 
The best route is the one that has the average temperature and the lowest cost. The program will output the best route and the average temperature of the trip.
"""

from itertools import permutations, combinations_with_replacement
from json import load

with open("city_temp_dist.json") as file:
    cities = load(file) 
with open("hotel_rates.json") as file:
    hotel_rates = load(file)

HOTEL_BUDGET = 850
avgTempCitiesList = []
routes = ""
hotels = ""

def avg_temp(routes: tuple) -> float:
    c = int(0)       
    for cities in routes:  
        temps = cities['temp']    
        avgTempCitiesList.append(temps[c])
        c+=1
    finalTemp = lambda avgTemp: avgTemp / len(avgTempCitiesList)
    return round(finalTemp(sum(avgTempCitiesList)), 2)

def best_route() -> tuple:
    best_route_temp = 0
    best_route_hotel = 0
    for route in permutations(cities, len(cities)):
        if avg_temp(route) > best_route_temp:
            best_route_temp = avg_temp(route)
            best_route_hotel = 0
            for hotel in combinations_with_replacement(hotel_rates, len(cities)):
                if sum([h['price'] for h in hotel]) < HOTEL_BUDGET:
                    if sum([h['price'] for h in hotel]) > best_route_hotel:
                        best_route_hotel = sum([h['price'] for h in hotel])
                        best_route = route
    return best_route

def total_cost(routes: tuple) -> float:
    total_cost = 0
    for hotel in combinations_with_replacement(hotel_rates, len(cities)):
        if sum([h['price'] for h in hotel]) < HOTEL_BUDGET:
            if sum([h['price'] for h in hotel]) > total_cost:
                total_cost = sum([h['price'] for h in hotel])
    return total_cost


def main():
    print("Road Trip Planner By Nolan")
    print("Cities:")
    for city in cities:
        print(f"\t{city['name']}")
    print("Hotels:")
    for hotel in hotel_rates:
        print(f"\t{hotel['name']}: ${hotel['price']}")
    print("Budget: $", HOTEL_BUDGET)
    print("Calculating best route...")
    best_route()
    print("Best Route:", " -> ".join([city['name'] for city in best_route()]))
    print("Average Temperature:", avg_temp(best_route()), "F")
    # print each hotel in the best route
    print("Hotels In Order:")
    best_route_hotel = 0
    for hotel in combinations_with_replacement(hotel_rates, len(cities)):
        if sum([h['price'] for h in hotel]) < HOTEL_BUDGET:
            if sum([h['price'] for h in hotel]) > best_route_hotel:
                best_route_hotel = sum([h['price'] for h in hotel])
                hotels = hotel
    for hotel in hotels:
        print(f"\t{hotel['name']}: ${hotel['price']}")
    print("Total Hotel Cost: $", total_cost(best_route()))
    return

if __name__ == '__main__':  
    main()