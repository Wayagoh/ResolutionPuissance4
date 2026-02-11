import numpy as np

class Game:
	def __init__(self, rows = 6, cols = 7):
		self.rows = rows
		self.cols = cols
		self.board = np.zeros((self.rows,self.cols), dtype=int)
		# self.board[-1,0]=1
		self.turn = 1
		# print(self.board)


	def get_turn(self):
		return self.turn

	def next_turn(self):
		self.turn = self.turn + 1

	def which_turn(self):
		temp = self.turn % 2
		if temp == 0:
			temp = 2
		return temp

	def do_action(self, col, id_player):
		valid_action = 0
		for i in range(-1, -self.rows - 1, -1):
			if self.board[i, col] == 0:
				self.board[i, col] = id_player
				valid_action = 1
				break
		if valid_action == 0:
			raise Exception("Invalid action")
		self.next_turn()
		return True

	def get_possible_actions(self):
		possible_actions = []
		board = self.get_board()
		line=board[0]
		for i in range(0, line.size):
			if line[i] == 0:
				possible_actions.append(i)
		return possible_actions


	def get_board(self):
		return self.board

	def show_board(self):
		print(self.board)

	def possible_actions(self):
		possible_actions = []
		for i in range(0, self.rows):
			if self.board[0, i]	== 1:
				possible_actions.append(i)
		return possible_actions

	def fill_list(self, list_to_fill):
		max_length = 0
		for i in range(0, len(list_to_fill)):
			if len(list_to_fill[i]) > max_length:
				max_length = len(list_to_fill[i])
		for i in range(0, len(list_to_fill)):
			while len(list_to_fill[i]) < max_length:
				list_to_fill[i].append(0)


	def line_checking(self, line):
		size = line.size
		token = 0
		counter = 0
		win = False
		# print(line)
		for i in range(0, size): #Faire un case match pour faire plus beau et peut-être causer moins de problèmes
			if line[i] == 0:
				counter = 0
			if line[i] == token and line[i] != 0: # Ne pas changer les if sinon compteur commence à 2.
				counter +=1
			if line[i] != token and line[i] != 0:
				counter = 1
				token = line[i]
			if counter == 4:
				win = True
				break
			# print(token ,counter)
		if token != 0 and win == False: #Sert à éviter les .items sur des int qui causent des erreurs
			token = 0
		return win, token


	def horizontal_checking(self, board = None):
		if board is None:
			board = self.board
		win = False
		id_winner = 0
		rows = board.shape[0]
		for i in range(-1, -rows -1, -1):
			win, id_winner = self.line_checking(board[i])
			if win:
				return win, id_winner.item() #Arrête le calcul dès que possible, la méthode sert à obtenir un int plutôt qu'un np.int64, ce qui arrive quand il y a un gagnant (token, ou id_winner != 0)
		return win, id_winner

	def vertical_checking(self, board = None):
		if board is None:
			board = np.transpose(self.board)
		return self.horizontal_checking(board)

	def diagonal_blfr_checking(self, board = None): #Diagonale partant d'en bas à gauche à en haut à droite
		if board is None:
			board = self.board
		list_diag = []
		list_diag_temp = []
		rows = board.shape[0]
		cols = board.shape[1]
		for i in range (3, rows-1):
			k=0 #j
			t=i #i
			while t>=0 and k<cols:
				list_diag_temp.append(board[t,k].item())
				k+=1
				t-=1
			list_diag.append(list_diag_temp.copy())
			list_diag_temp = []
		for j in range (0, cols-3):
			k=rows-1 #i
			t=j #j
			while k>=0 and t<cols:
				list_diag_temp.append(board[k,t].item())
				k-=1
				t+=1
			list_diag.append(list_diag_temp.copy())
			list_diag_temp = []
		print(list_diag)
		self.fill_list(list_diag)
		print(list_diag)
		list_diag=np.asarray(list_diag)
		return self.horizontal_checking(list_diag)

	def diagonal_flbr_checking(self, board = None): #Diagonale partant d'en haut à gauche à en bas à droite
		if board is None:
			board = self.board
		list_diag = []
		list_diag_temp = []
		rows = board.shape[0]
		cols = board.shape[1]
		for i in range(0, rows - 3):
			k = 0  # j
			t = i  # i
			while t <rows and k < cols:
				list_diag_temp.append(board[t, k].item())
				k += 1
				t += 1
			list_diag.append(list_diag_temp.copy())
			list_diag_temp = []
		for j in range(1, cols - 3):
			k = 0  # i
			t = j  # j
			while k <rows and t < cols:
				list_diag_temp.append(board[k, t].item())
				k += 1
				t += 1
			list_diag.append(list_diag_temp.copy())
			list_diag_temp = []
		print(list_diag)
		self.fill_list(list_diag)
		print(list_diag)
		list_diag = np.asarray(list_diag)
		return self.horizontal_checking(list_diag)

	def diagonal_checking(self, board = None):
		if board is None:
			board = self.board
		win = False
		id_winner = 0
		win, id_winner = self.diagonal_blfr_checking() #Plus de chance avec des joueurs humains de gagner dans ce sens de diagonal que l'autre (sens de lecture)
		if win:
			return win, id_winner
		win, id_winner = self.diagonal_flbr_checking()
		if win:
			return win, id_winner
		return win, id_winner

	def check_board(self):
		win = False
		id_winner = 0
		function_check = [
			self.horizontal_checking,
			self.vertical_checking,
			self.diagonal_checking
		]#Ordre optimisé car 4*6=24 cas de victoire pour la vérification horizontale, 3*7=21 pour la verticale et 1+2+3+3+2+1=12 pour chaque diagonale (24 pour les deux)
		#Ainsi en ordonnant par les cas les plus probables, nous sommes plus susceptible d'éviter des calculs inutils
		for func in function_check:
			win, id_winner = func()
			if win:
				return win, id_winner

		return win, id_winner




#Faire un truc plus propre pour les .items
#
# jeu = Game()
# jeu.do_action(0,1)
# jeu.do_action(1,1)
# jeu.do_action(2,1)
# jeu.do_action(2,1)
# jeu.do_action(2,1)
# jeu.do_action(3,1)
# jeu.do_action(3,1)
# jeu.do_action(3,1)
# jeu.do_action(3,2)
# jeu.do_action(1,1)
# jeu.do_action(0,1)
# jeu.do_action(0,1)
# jeu.do_action(6,1)
# jeu.do_action(1,1)
# jeu.do_action(0,1)

# print(jeu.get_board())
# print(jeu.get_board().shape)
# a=np.array([0,2,2,1,1,1])
# print(jeu.vertical_checking())
# print(jeu.diagonal_flbr_checking())
# print(jeu.diagonal_checking())
# print(jeu.check_board())
