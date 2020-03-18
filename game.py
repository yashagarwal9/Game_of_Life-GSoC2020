import time
import os
import random
import sys
import json
import numpy as np

class Game_of_Life:

	def __init__(self, cols, rows, generations, grid):
		self.grid = grid#np.random.randint(2, size=(rows,cols))
		self.rows = rows
		self.cols = cols
		self.generations = generations
		self.resize_terminal()

	def resize_terminal(self):
		cols = self.cols
		if cols < 32:
			cols = 32

		if sys.platform.startswith('linux'):
			command = "\x1b[8;{rows};{cols}t".format(rows=self.rows + 3, cols=cols + cols)
			sys.stdout.write(command)
		elif sys.platform.startswith('win'):
			command = "mode con: cols={0} lines={1}".format(cols + cols, self.rows + 5)
			os.system(command)
		else:
			print("Unable to resize terminal.\n")


	def print_grid(self):
		if sys.platform.startswith('linux'):
			os.system("clear")
		elif sys.platform.startswith('win'):
			os.system("cls")
		else:
			print("Unable to clear the terminal\n")

		output = ""
		output += "Generation {0} - To exit the program early press <Ctrl-C>\n\r".format(self.generations)
		for row in range(self.rows):
			for col in range(self.cols):
				if self.grid[row][col] == 0:
					output += ". "
				else:
					output += "# "
			output += "\n\r"
		print(output, end=" ")

	def next_grid(self, next_grid):
		for row in range(self.rows):
			for col in range(self.cols):
				live_neighbors = self.get_live_neighbors(row, col)
				# If the number of surrounding live cells is < 2 or > 3 then we make the cell at grid[row][col] a dead cell
				if live_neighbors < 2 or live_neighbors > 3:
					next_grid[row][col] = 0
				# If the number of surrounding live cells is 3 and the cell at grid[row][col] was previously dead then make
				# the cell into a live cell
				elif live_neighbors == 3 and self.grid[row][col] == 0:
					next_grid[row][col] = 1
				# If the number of surrounding live cells is 3 and the cell at grid[row][col] is alive keep it alive
				else:
					next_grid[row][col] = self.grid[row][col]
		return next_grid

	def get_live_neighbors(self, row, col):
		life_sum = 0
		for i in range(-1, 2):
			for j in range(-1, 2):
				# Make sure to count the center cell located at grid[row][col]
				if not (i == 0 and j == 0):
					# Using the modulo operator (%) the grid wraps around
					life_sum += self.grid[((row + i) % self.rows)][((col + j) % self.cols)]
		return life_sum

	def grid_changing(self, next_grid):
		for row in range(self.rows):
			for col in range(self.cols):
				# If the cell at grid[row][col] is not equal to next_grid[row][col]
				if not self.grid[row][col] == next_grid[row][col]:
					return True
		return False


	def run(self):
		next_gen = np.random.randint(2, size=(rows,cols))
		for gen in range (self.generations):
			if not self.grid_changing(next_gen):
				break
			self.print_grid()
			next_gen = self.next_grid(next_gen)
			time.sleep(1/5.0)
			self.grid, next_gen = next_gen , self.grid
		self.print_grid()
		input("Press <Enter> to exit.")


if __name__ == '__main__':

	with open('./config.json') as f:
		data = json.load(f)

	if data['pattern_file_name'] == "" :
		print("Enter the path of the file containing initial patten")
		exit()
	grid = np.loadtxt(data['pattern_file_name'], dtype='i', delimiter=',')

	if data['generations'] < 1 or data['generations'] > 10000:
		print("Enter the number of generations in between 1 and 10000")
		exit()
	generations = data['generations']

	rows, cols = grid.shape	

	game = Game_of_Life(cols, rows, generations, grid)
	game.run()
