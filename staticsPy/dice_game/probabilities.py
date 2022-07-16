from typing import *

class Probability:
    dices: List[int]        
    
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
        triad_number: int = 0
        triad_count: int = 0
        pair_number: int = 0
        pair_count: int = 0
        dices_repeated: List[int] = []
        
        for x in self.dices:
            if (dices_repeated.count(x) != 0):
                continue
            
            if (self.dices.count(x) >= triad_count):
                pair_number = triad_number
                pair_count = triad_count
                triad_number = x
                triad_count = self.dices.count(x)
                
            dices_repeated.append(x)
        
        if (pair_count == 0):
            dices_repeated.clear()
            for x in self.dices:
                if ((x == triad_number) or (dices_repeated.count(x) != 0)):
                    continue
                if (self.dices.count(x) >= pair_count):
                    pair_count = self.dices.count(x)
                    pair_number = x
                dices_repeated.append(x)
                    
        key_str: str = "Keeping dices with number: " + str(triad_number) + " and " + str(pair_number)
        probability: float = 0.0
        
            
        if (triad_count < 3):
            probability = (triad_count / 3) * (pair_count / 2)
        else:
            probability = pair_count / 2
        
        return {
            key_str: probability
        }
                
            
        
    def in_order(self) -> Dict[str, float]:
        unique_dices: List[int] = []
        
        for x in self.dices:
            if (unique_dices.count(x) == 1):
                continue
            unique_dices.append(x)
        
        key_str: str = "Keeping dices with number: "
        
        for x in unique_dices:
            
            if (unique_dices.index(x) == (len(unique_dices) - 1)):
                key_str += str(x)                
            elif (unique_dices.index(x) == (len(unique_dices) - 2)):
                key_str = key_str + (str(x) + " and ")
            else:
                key_str = key_str + (str(x) + ", ")
                
        probability: float = 0.0
        reapeted_dices_count: int = len(self.dices) - len(unique_dices)
                                     
        for _ in range(reapeted_dices_count):
            #TODO: FIX THIS PROBABILITY, I NEED TO USE CONDITIONAL PROBABILITY
            probability += 1 / 6
    
        return {
            key_str: probability
        }
        
        
    def show_probabilities(self) -> None:
        results: Dict[str, Dict[str, float]] = {}
        
        results["generala"] = self.generala()
        results["poker"] = self.poker()
        results["full"] = self.full()
        results["in order"] = self.in_order()
        
        print(results)

    def set_dices(self, dices_values: List[int]) -> None:
        self.dices = dices_values    
        
    
        