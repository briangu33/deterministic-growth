import numpy as np
import math

class Point:

	def __init__(self, x, y, index = -1):
		self.x = x
		self.y = y
		self.index = index

	def adjacent(self):
		ret = [Point(self.x - 1, self.y, self.index + 1), \
		Point(self.x, self.y - 1, self.index + 1), \
		Point(self.x + 1, self.y, self.index + 1), \
		Point(self.x, self.y + 1, self.index + 1)]

		return ret

	def __hash__(self):
		return hash((self.x, self.y))

	def __eq__(self, other):
		return (self.x, self.y) == (other.x, other.y)

	def __repr__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"

def get_Xs(N_TIMESTEPS):
	X = [[Point(0, 0, 0)]]
	for timestep in range(N_TIMESTEPS):
		X_append = []
		candidates = []
		for point in X[timestep]:
			X_append.append(point)
			adjacents = point.adjacent()
			for adjacent in adjacents:
				candidates.append(adjacent)
		candidates = get_only_unique(candidates)
		for candidate in candidates:
			if candidate not in X[timestep]:
				X_append.append(candidate)
		X.append(X_append)
	return X

def get_only_unique(arr):
	d = dict()
	for a in arr:
		if a not in d:
			d[a] = 1
		else:
			d[a] += 1
	ret = []
	for a in arr:
		if d[a] == 1:
			ret.append(a)
	return ret

def get_grid(N_TIMESTEPS, MAX_COORD):
	grid = np.array([[-1 for i in range(2 * MAX_COORD + 1)] for j in range(2 * MAX_COORD + 1)])
	X = get_Xs(N_TIMESTEPS)[-1]
	for point in X:
		if math.fabs(point.x) <= MAX_COORD and math.fabs(point.y) <= MAX_COORD:
			grid[MAX_COORD + point.x][MAX_COORD + point.y] = point.index
	return grid

print(get_grid(35, 10))

