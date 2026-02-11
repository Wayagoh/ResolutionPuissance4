import numpy as np

import Game.player
import Game.game

class RandomPlayer(Game.player.Player):
	def __init__(self, id):
		super().__init__(id)



	def compute_action(self, game:Game.game.Game):
		possible_actions = game.get_possible_actions()
		n = len(possible_actions)
		action = possible_actions[np.random.randint(0,n-1)]
		return action