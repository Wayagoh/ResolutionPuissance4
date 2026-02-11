import Game.game
import Game.player
import Game.human_player
import numpy as np


def get_input(id_joueur):
	action = -1
	while action<0 or action>6:
		answer: str = input(f' Joueur {id_joueur}, dans quelle colonne souhaitez-vous jouer? ')
		action = int(answer)
		if action<0 or action>6:
			print('Veuillez saisir un nombre entre 0 et 6')
	return action

def main():
	jeu=Game.game.Game()
	player1= Game.human_player.HumanPlayer(1)
	player2= Game.human_player.HumanPlayer(2)
	players=[player1,player2]

	max_turn=jeu.get_board().size
	win=0
	id=0
	w=False
	while jeu.get_turn()<=max_turn and win==0:
		jeu.show_board()
		t=jeu.which_turn()-1
		# action=get_input(t)
		action=players[t].compute_action(jeu)
		jeu.do_action(action,t+1)
		if jeu.get_turn()>=7:
			w,id=jeu.check_board()
		if w:
			win=1

	if win==1:
		print(f'Le joueur {id} a gagné')
	else:
		print('égalité')





main()