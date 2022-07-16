from game import Game
from probabilities import Probability

game = Game(3)
probabilities = Probability()

while (game.rolls != 0):
    print("***********************************")
    dices = game.roll_dices()
    probabilities.set_dices(dices)
    
    probabilities.show_probabilities()
    if (game.rolls == 0):
        continue
    game.choose_dices()

    