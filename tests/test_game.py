# import pytest
import Game.game as game

def main():
	jeu=game.Game()
	jeu.board[0,0]=1
	print(jeu.get_possible_actions())
	jeu.show_board()

main()

def test_get_possible_actions1():
	jeu=game.Game()
	jeu.board[0, 0] = 1
	assert jeu.get_possible_actions() == [1, 2, 3, 4, 5, 6]


