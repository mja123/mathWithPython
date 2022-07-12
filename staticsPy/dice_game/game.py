import random
from typing import *

dices_values: List[int] = []

def roll_dices():
    rolls: int = 3
    
    if (rolls != 0):
        for _ in range(5):
            dices_values.append(random.randint(1, 6))
            rolls -= 1
        print(f'First roll: {dices_values}')

def choose_dices():
    change: bool = input("Do you want to change some dice? ")
    
    if (change):
        change_dices: int = input("Which dices do you want to change? ")
        
        for _ in range(change_dices):
            
            
        

if (__name__ == "__main__"):
    roll_dices()
    
        

