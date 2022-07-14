from distutils.util import execute
from random import *
from typing import *

class Game:
    rolls: int
    dices_values: List[int]
    saved_dices: List[int]
    execute: bool
    
    def __init__(self, rolls: int) -> None:
        self.rolls = rolls        
        self.saved_dices = []
        self.dices_values = []
        self.execute = True
        
    def roll_dices(self) -> List[int]:
   
        if (self.rolls != 0):
            if (self.rolls == 3):
                for _ in range(5):
                    self.dices_values.append(randint(1, 6))    
            else:
                values_copy: List[int] = self.dices_values.copy()
                
                for dice in values_copy:
                    if (dice in self.saved_dices):                    
                        continue
                    self.dices_values.remove(dice)
                    self.dices_values.append(randint(1, 6))
                        
            
            self.rolls -= 1
            
            print(f'Dices values: {self.dices_values}')
            return self.dices_values
            
        else:
            self.execute = False
            return self.dices_values

    def choose_dices(self) -> None:
        change_dices: List[int] = []
        self.saved_dices.clear()
        changes: str = input("Which dices do you want to change? (0 for no changes) ")
        
        for x in changes:    
            if (x == " "):
                continue
            change_dices.append(int(x))
            
        
        if ((len(change_dices) == 1) and (0 in change_dices)):
            self.execute = False
        
        for dice in self.dices_values:
            if (dice not in change_dices):
                self.saved_dices.append(dice)
        
        
    def roll_result(self) -> List[int]:
        return self.dices_values
    
    def get_dices_values(self) -> List[int]:
        return self.dices_values

    
    
    
        

