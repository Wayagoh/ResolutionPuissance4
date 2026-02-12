import Game.game
import Game.player
import Game.human_player
import Game.random_player
import numpy as np
import sys
import getopt




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

	try:
		opts, args = getopt.getopt(sys.argv[1:], "p:q:t",["player1=","player2=","terminal"])
	except getopt.GetoptError as err:
		print(err)
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-p", "--player1"):
			match arg:
				case "human":
					player1 = Game.human_player.HumanPlayer(1)
				case "random":
					player1 = Game.random_player.RandomPlayer(1)
				case _:
					print("Commande non valide pour le joueur 1, joueur humain choisi par défaut")
					player1 = Game.human_player.HumanPlayer(1)
		elif opt in ("-q", "--player2"):
			match arg:
				case "human":
					player2 = Game.human_player.HumanPlayer(2)
				case 'random':
					player2 = Game.random_player.RandomPlayer(2)
				case _:
					print("Commande non valide pour le joueur 2, joueur humain choisi par défaut")
					player2 = Game.human_player.HumanPlayer(2)
		elif opt in ("-t", "--terminal"):
			print("Mode terminal activé")


	# jeu=Game.game.Game()
	# player1= Game.human_player.HumanPlayer(1)
	# player2= Game.human_player.HumanPlayer(2)
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

		print(f'\033[33mLe joueur {t+1} a joué\033[0m')
		if jeu.get_turn()>=7:
			w,id=jeu.check_board()
		if w:
			win=1

	if win==1:
		print(f'Le joueur {id} a gagné')
	else:
		print('égalité')




if __name__ == '__main__':
	print(sys.argv[1:])
	main()