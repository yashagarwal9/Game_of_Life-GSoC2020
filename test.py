from game import Game_of_Life
import numpy as np
import unittest

class GameofLifeTest(unittest.TestCase):
	def test_EmptyGrid(self):
		temp = [[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0]]

		grid = [[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0]]

		desired = [[0,0,0,0,0],
				  [0,0,0,0,0],
				  [0,0,0,0,0],
				  [0,0,0,0,0]]

		game = Game_of_Life(5,4,1,grid)
		actual = game.next_grid(temp)
		self.assertEqual(actual, desired)

	def test_Single_next_grid(self):
		temp = [[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0]]

		grid = [[1,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0]]

		desired = [[0,0,0,0,0],
				  [0,0,0,0,0],
				  [0,0,0,0,0],
				  [0,0,0,0,0]]

		game = Game_of_Life(5,4,1,grid)
		actual = game.next_grid(temp)
		self.assertEqual(actual, desired)

	def test_next_grid(self):
		temp = [[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0]]

		grid = [[0,0,0,0,0],
				[0,0,1,0,0],
				[0,0,1,0,0],
				[0,0,1,0,0],
				[0,0,0,0,0]] 

		desired = [[0,0,0,0,0],
				  [0,0,0,0,0],
				  [0,1,1,1,0],
				  [0,0,0,0,0],
				  [0,0,0,0,0]]

		game = Game_of_Life(5,5,1,grid)
		actual = game.next_grid(temp)
		self.assertEqual(actual, desired)


	def test_get_live_neighbours(self):
		temp = [[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0]]

		grid = [[0,0,0,0,0],
				[0,1,1,0,0],
				[0,1,1,0,0],
				[0,0,0,0,0],
				[0,0,0,0,0]] 

		desired = 3

		game = Game_of_Life(5,5,1,grid)
		actual = game.get_live_neighbors(1,1)
		self.assertEqual(actual, desired)


if __name__ == '__main__':
    unittest.main()