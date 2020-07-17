import pygame, math 
from queue import PriorityQueue

# set a var to hold width for pygame window
WIDTH = 800
# initialize the window as a pygame display with width x width
WIN = pygame.display.set_mode((WIDTH, WIDTH))

# caption for the window
pygame.display.set_caption("A* Pathfinding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# the individual components on the windo
class Spot:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		# all spots initialize white
		self.color = WHITE
		# neighbor nodes
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	# fn to get the position to be able to draw the spot
	def get_pos(self):
		return self.row, self.col

	# this tells us the state of the spot, if we have been to it or not
	def is_closed(self):
		return self.color == RED
		# if red, been there
		# if white, not been there
		# black is barrier

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == TURQUOISE

	def reset(self):
		self.color = WHITE

	def make_closed(self):
		self.color = RED

	def make_open(self):
		self.color = GREEN

	def make_barrier(self):
		self.color = BLACK

	def make_start(self):
		self.color = ORANGE

	def make_end(self):
		self.color = TURQUOISE

	def make_path(self):
		self.color = PURPLE

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		# check up, down, left, right if are barriers
		self.neighbors = []

		# check to make sure we aren't on an edge, then check if the spot below is a barrier
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])


	# less than, if you compare two of these classes will return false
	def __lt__(self, other):
		return False


# heuristic function
def h(p1, p2):
	# (row, col)
	# break out the components of p1 and p2
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
	# current node starts at end node
	while current in came_from:
		# set current to the value that we came from to get to current
		current = came_from[current]
		# change the color of current to path color
		current.make_path()
		# update the window
		draw()

def algorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	# initialize the queue
	open_set.put((0, count, start))

	# keeps track of the path, where we came from
	came_from = {}

	# dict comprehension to initialize g score
	# keeps track of the current shortest distance from the start to the cur node
	g_score = {spot: float("inf") for row in grid for spot in row}
	# first node g_score is 0 because it is 0 away from the start
	g_score[start] = 0

	# dict comprehension to initialize f score
	# keeps track of predicted distance from this node to end node
	f_score = {spot: float("inf") for row in grid for spot in row}
	# fscore initialized at h(n) because we want to estimate distance from start to end
	f_score[start] = h(start.get_pos(), end.get_pos())

	# keep track of items in PrioQ, since we cannot peak into the PrioQ
	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			# exit the loop if click exit
			if event.type == pygame.QUIT:
				pygame.quit()
		# grab the current value from the open set, pops the value
		# use [2] because that the Node
		current = open_set.get()[2]
		# sync the hash table
		open_set_hash.remove(current)

		# terminus, if we can find a path back
		if current == end:
			#make path back
			reconstruct_path(came_from, end, draw)
			# recolor end
			end.make_end()
			return True

		# if not on the end node, examin the neighbors
		# find the neighbor with lowest gscore
		for neighbor in current.neighbors:
			# add 1 for all the available neighbors, adding 'depth' from the start
			temp_g_score = g_score[current] + 1

			# look if the gscore of current is lower than the neighbor
			if temp_g_score < g_score[neighbor]:
				# add the path we took to get to current to the came_from dict, used to reconstruct path later
				came_from[neighbor] = current
				# update the gscore to reflect movement
				g_score[neighbor] = temp_g_score
				# update the fscore to reflect movement
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				# check if we have seen the neighbor node before
				# if not, add to count, add it to the PrioQ and the hash table.
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		# update the window
		draw()
		# update the color of the current square to show we have been to it.
		if current != start:
			current.make_closed()

	return False


# make the grid of the game
def make_grid(rows, width):
	grid = []
	gap = width // rows
	# loop to generate the rows
	for i in range(rows):
		# empty list that will hold the rows values
		grid.append([])
		# generate the 'width' as a list to be populated
		for j in range(rows):
			# create spots in each sublist
			spot = Spot(i, j, gap, rows)
			# add the new spot to the current row 
			grid[i].append(spot)
	return grid

def draw_grid(win, rows, width):
	gap = width // rows

	# draw horizontal grid lines
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		# draw vertical grid lines
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

# main draw function, draws the game window
def draw(win, grid, rows, width):
	win.fill(WHITE)
	for row in grid:

		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	# updates the pygame window
	pygame.display.update()

# takes mouse position and what spot we are interacting with
def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos
	# relating the x,y position to the appropriate square
	row = y // gap
	col = x // gap

	return row, col

# main game loop
def main(win, width):
	# desired number of rows for the game
	ROWS = 25
	# initialize the game grid
	grid = make_grid(ROWS, width)
	# variables for start node and end node
	start = None
	end = None
	# game state variables
	run = True
	started = False

	# game loop
	while run:
		# draws the window every iteration
		draw(win, grid, ROWS, width)

		# loop through events that the window gets
		for event in pygame.event.get():
			# check if someone exits the game
			if event.type == pygame.QUIT:
				run = False

			# left mouse button pressed
			if pygame.mouse.get_pressed()[0]:

				pos = pygame.mouse.get_pos()
				# gives us the spot we clicked on
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]

				# if there is no start position defined, first click is the start
				if not start and spot != end:
					start = spot
					start.make_start()

				# if there is no end position, second click is the end
				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			# right mouse button pressed
			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				# gives us the spot we clicked on
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				# right click to clear the spot
				spot.reset()
				# reset the start in game loop
				if spot == start:
					start = None
				# reset the end in the game loop
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					# run the algorithm

					# on press space, update all the neighbors of all spots
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

				# reset the board
				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)


	pygame.quit()

main(WIN, WIDTH)