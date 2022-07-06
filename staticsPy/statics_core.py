from math import sqrt
import random
from typing import *

#TODO: Transform this code in one class.
# class Statics_core {

# }

def average(X: List[int]) -> float:
    return sum(X) / len(X)

def variance(X: List[int]) -> float:
    sum_of_differences: float = 0
    mu: float = average(X)
    
    #x = sample (element in the list), X = the list of samples, mu = mean
    for x in X:
        #(x - mun)**2 = deviation
        sum_of_differences += (x - mu)**2
        
    return sum_of_differences / len(X)
        
def standard_deviation(X: List[int]) -> float:
    return sqrt(variance(X))

if (__name__ == "__main__"):
    X: List[int] = [random.randint(1, 101) for i in range(100)]
    print(X)
    print(f'The average of the random list is: {average(X)}')
    print(f'The variance of the random list is: {variance(X)}')
    print(f'The standard deviation of the random list is: {standard_deviation(X)}')