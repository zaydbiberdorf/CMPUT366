from math import inf
import random
import unittest 
from connect4 import Board

def otherPlayer(player):
	"""
	returns the next player to play
	"""
	if player == 'X':
		return 'O'
	else:
		return 'X'

def minimax(board, player, ply):
	"""
	Function receives an instances of the Board class, the player who is to act at this state (either X or O),
	and the maximum search depth given by the variable ply.

	The function returns three values: 
	1. the score of the optimal move for the player who is to act;
	2. the optimal move
	3. the total number of nodes expanded to find the optimal move 
	"""
	# getting the algorithem to stop at depth 0
	if ply == 0:
		# return the score if bord is terminal otherwise return regular inf or -inf score
		if board.is_terminal():
			gameValue = board.game_value()
			return gameValue, 0, 1
		else:
			if player == 'X':
				return inf, 0, 1
			elif player == 'O':
				return -inf, 0, 1

	# checking if board is terminal
	if board.is_terminal():
		gameValue = board.game_value()
		return gameValue, 0, 1
	
			
			
		
	# setting u based on which players turn it is
	if player == 'X':
		u = [-inf, -inf, -inf, -inf, -inf, -inf, -inf]
	elif player == 'O':
		u = [inf, inf, inf, inf, inf, inf, inf]

	totExp = 0
	
	# going through each avalibel action and getting setting score in u based on branches of the tree
	for a in board.available_moves():
		board.perform_move(a, player)
		score, move, expansions = minimax(board, otherPlayer(player), ply - 1)	
		totExp += expansions
		board.undo_move(a)

		u[a] = score
	
	# setting the score based on which players turn it is
	if player == 'X':
		score = max(u)
	elif player == 'O':
		score = min(u)

	return score, u.index(score), totExp

class TestMinMaxDepth1(unittest.TestCase):


	def test_depth1a(self):
		b = Board()
		player = b.create_board('010101')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 0)

	def test_depth1b(self): 
		b = Board() 
		player = b.create_board('001122')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 3)

	def test_depth1c(self): 
		b = Board() 
		player = b.create_board('335566')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 4)

	def test_depth1d(self):
		b = Board() 
		player = b.create_board('3445655606')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 6)

	def test_depth1e(self):
		b = Board() 
		player = b.create_board('34232210101')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 1)

	def test_depth1f(self):
		b = Board() 
		player = b.create_board('23445655606')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 6)

	def test_depth1g(self): 
		b = Board() 
		player = b.create_board('33425614156')
		bestScore, bestMove, expansions = minimax(b, player, 1)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 2)

class TestMinMaxDepth3(unittest.TestCase):

	def test_depth3a(self):
		b = Board()
		player = b.create_board('303111426551')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 2)

	def test_depth3b(self): 
		b = Board() 
		player = b.create_board('23343566520605001')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 6)

	def test_depth3c(self): 
		b = Board() 
		player = b.create_board('10322104046663')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 0)

	def test_depth3d(self):
		b = Board() 
		player = b.create_board('00224460026466')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 3)

	def test_depth3e(self):
		b = Board() 
		player = b.create_board('102455500041526')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 1)

	def test_depth3f(self):
		b = Board() 
		player = b.create_board('01114253335255')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 2)

	def test_depth3g(self): 
		b = Board() 
		player = b.create_board('0325450636643')
		bestScore, bestMove, expansions = minimax(b, player, 3)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 5)

class TestMinMaxDepth5(unittest.TestCase):
	def test_depth5a(self):
		b = Board()
		player = b.create_board('430265511116')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 3)
		
	def test_depth5b(self):
		b = Board()
		player = b.create_board('536432111330')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 5)

	def test_depth5c(self):
		b = Board()
		player = b.create_board('322411004326')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 3)

	def test_depth5d(self):
		b = Board()
		player = b.create_board('3541226000220')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 4)

	def test_depth5e(self):
		b = Board()
		player = b.create_board('43231033655')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, -1)
		self.assertEqual(bestMove, 1)

	def test_depth5f(self):
		b = Board()
		player = b.create_board('345641411335')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 5)

	def test_depth5g(self):
		b = Board()
		player = b.create_board('336604464463')
		bestScore, bestMove, expansions = minimax(b, player, 5)
		print(b)
		print(expansions)
		self.assertEqual(bestScore, 1)
		self.assertEqual(bestMove, 3)		


if __name__ == '__main__':
    unittest.main()
