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
		self.color == WHITE

	def make_close(self):
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
		pass

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
	ROWS = 50
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
			# check if the algo has started to optimize path
			# stops from changing the obstacles while on the path
			if started:
				continue

			# left mouse button pressed
			if pygame.mouse.get_pressed()[0]:

				pos = pygame.mouse.get_pos()
				# gives us the spot we clicked on
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]

				# if there is no start position defined, first click is the start
				if not start:
					start = spot
					start.make_start()

				# if there is no end position, second click is the end
				elif not end:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			# right mouse button pressed
			elif pygame.mouse.get_pressed()[2]:
				pass

	pygame.quit()

main(WIN, WIDTH)