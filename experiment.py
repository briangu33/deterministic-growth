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

def run_experiment(N_TIMESTEPS, MAX_COORD):
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

print(run_experiment(2, 10))

