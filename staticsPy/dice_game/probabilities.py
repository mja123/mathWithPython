from typing import *

class Probability:
    dices: List[int]
    
    # def __init__(self) -> None:
        
    
    def generala(self) -> Dict[str, float]:
        count_dices: int = 0
        number: int = 0
        
        for x in self.dices:
            if (self.dices.count(x) > count_dices):
                count_dices = self.dices.count(x)
                number = x
        
        key_str: str = "Keeping dice/s with number: " + str(number)
        
        
        return {
            key_str: count_dices / len(self.dices)
        }
        
            
    def poker(self) -> Dict[str, float]:
        count_dices: int = 0
        number: int = 0
        
        for x in self.dices:
            if (self.dices.count(x) > count_dices):
                count_dices = self.dices.count(x)
                number = x
        
        key_str: str = "Keeping dice/s with number: " + str(number)
        
        return {
            key_str: count_dices / (len(self.dices) - 1)
        }
        
    def full(self) -> Dict[str, float]:
        pass
    def in_order(self) -> Dict[str, float]:
        pass
    
    def show_probabilities(self) -> None:
        results: Dict[str, Dict[str, float]] = {}
        
        results["generala"] = self.generala()
        results["poker"] = self.poker()
        # results["full"] = self.full()
        # results["in order"] = self.in_order()
        
        print(results)

    def set_dices(self, dices_values: List[int]) -> None:
        self.dices = dices_values    
        
    
        