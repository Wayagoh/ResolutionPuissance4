import Game.game

class Player:
	def __init__(self, id):
		self.id = id

	def get_id(self):
		return self.id

	def compute_action(self, game:Game.game.Game):
		pass

