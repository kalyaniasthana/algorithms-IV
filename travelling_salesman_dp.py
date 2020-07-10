'''
The first line indicates the number of cities.
Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.
'''
from itertools import product, chain, combinations
import math
import matplotlib.pyplot as plt
import numpy as np
import sys
import tsp

# read TSP input file
def read_tsp_file(filename):
	coordinates = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines[1: ]:
			l = line.strip('\n').split(' ')
			coordinates += [(float(l[0]),float(l[1]))]
	return coordinates

# euclidean distance between two points
def euclidean_distance(x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# plot TSP graph with distances
def plot_cities_with_distance(coordinates):
	fig, ax = plt.subplots()
	for point in coordinates:
		ax.scatter(point[0],point[1])

	for a, b in product(coordinates, coordinates):
		x = np.linspace(a[0], b[0], 100)
		y = np.linspace(a[1], b[1], 100)
		# print(x, y)
		dist = euclidean_distance(a[0],a[1],b[0],b[1])
		s = "%.2f"%dist
		m = [(a[i]+b[i])/2. for i in (0, 1)]
		ax.plot(x, y)
		if dist>0:
			ax.text(m[0], m[1], s)
	plt.show()

def tsproblem(coordinates):
	return tsp.tsp(coordinates)

if __name__ == '__main__':
	filename = sys.argv[1]
	coordinates = read_tsp_file(filename)
	print(tsproblem(coordinates))