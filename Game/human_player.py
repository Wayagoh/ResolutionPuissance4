import Game.player
import Game.game

class HumanPlayer(Game.player.Player):
	def __init__(self, id):
		super().__init__(id)

	def get_input(self, id_joueur, possible_actions):
		while True:
			answer: str = input(f' Joueur {id_joueur}, dans quelle colonne souhaitez-vous jouer? ')
			action = int(answer)
			if action not in possible_actions:
				print('Veuillez saisir un nombre correct')
			else:
				return action


	def compute_action(self, game:Game.game.Game):
		possible_actions = game.get_possible_actions()
		return self.get_input(super().get_id(), possible_actions)

