from genericpath import exists
from random import randint as rand
import json

#Store the results of the roll's results
def simulation(roll_count, simulation_count):
    simulation_results = []
    
    for _ in range(simulation_count):        
        simulation_results.append(roll_dice(roll_count))

    probability(simulation_results, roll_count)    


#Return the results of the rolls
def roll_dice(roll_count):
    dice_results = []
    
    for _ in range(roll_count):
        dice_results.append(rand(1, 7)) 
    return dice_results

            
#Calculate the probability of one number
def probability(simulation_results, roll_count):
    number = int(input("Which result of roll do you want to know the probability?: "))
    dice_face_counter = 0
    
    for roll in simulation_results:
        if (number in roll):
            dice_face_counter +=1
    
    simulation_count = len(simulation_results)
    result = dice_face_counter / simulation_count
    
    print(f"The probability to obtain {number} in {roll_count} rolls is: {result}.")
    
    store_results(number, roll_count, result, simulation_count, dices=1)


def store_results(number, roll_count, result, simulation_count, dices):
        with open("probabilities_results.json", "a+", encoding="utf-8") as file:
            data = {
                    "rolls": roll_count,
                    "dices": dices,
                    "simulation": simulation_count,
                    "number": number,
                    "probability": result
                    }
            file.seek(0)
            exists_data = file.read()
            print(exists_data)


            if (len(exists_data) == 0):           
                data_string = "["
                data_string += (json.dumps(data) + "]")
                file.write(data_string)
                
            else:
                
                data_string = json.dumps(data)
                exists_data = exists_data.removesuffix("]")
                data_string = exists_data + ", " + data_string + "]"
                fill_file(data_string)
                
            
def fill_file(data):
    with open("probabilities_results.json", "w", encoding="utf-8") as file:
        file.write(data)


if (__name__ == '__main__'): 
    roll_count = int(input("How many rolls do you want to do?: "))
    simulation_count = int(input("How many times do you want to execute the simulation?: "))
    result = simulation(roll_count, simulation_count)
