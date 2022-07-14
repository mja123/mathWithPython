from game import Game
from probabilities import Probability

game = Game(3)
probabilities = Probability()

while (game.rolls != 0):
    dices = game.roll_dices()
    probabilities.set_dices(dices)
    
    if (game.rolls == 0):
        continue
    probabilities.show_probabilities()
    game.choose_dices()

    