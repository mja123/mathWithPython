from math import pi
import random
from typing import *

def needle_thrower(needles_count: int) -> int:
    inside_circle: int = 0
    
    for _ in range(needles_count):
        needle_x: float = random.uniform(-1, 1)    
        needle_y: float = random.uniform(-1, 1)    
        
        distance: float = ((needle_x ** 2) + (needle_y ** 2)) ** 0.5
        
        if (distance < 1) :
            inside_circle += 1
    return inside_circle

def simulation(needles_count: int, simulation_count: int) -> float:
    
    pi_results: List[float] = []
    for _ in range(simulation_count):
        pi_results.append((4 * needle_thrower(needles_count)) / needles_count)
    
    return sum(pi_results) / len(pi_results)

def precision(pi_simulation):
    PI = pi
    if (pi > pi_simulation):
        return ((pi_simulation / pi) * 100)
    return ((pi/pi_simulation) * 100)

if (__name__ == "__main__"):
    needles_count = int(input("How meany needles do you want to throw? "))
    simulation_count = int(input("How many times do you want to run the simulation? "))
    result = simulation(needles_count, simulation_count)
    print(f'Throwing {needles_count} needles, pi is: {result} and the presicion is: %{precision(result)}')
    