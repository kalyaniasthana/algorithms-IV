import sys
import numpy as np

def make_graph(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()
		line_0 = lines[0].strip('\n').split(' ')
		no_of_nodes = int(line_0[0])
		A = np.full((no_of_nodes + 1, no_of_nodes + 1), float('Inf'))
		for line in lines[1: ]:
			l = line.strip('\n').split(' ')
			A[int(l[0]), int(l[1])] = int(l[2])
			# print(A[int(l[0]), int(l[1])])

	np.fill_diagonal(A, 0)

	return no_of_nodes, A

def fw(no_of_nodes, A):

	for k in range(1, no_of_nodes + 1):
		for j in range(1, no_of_nodes + 1):
			for i in range(1, no_of_nodes + 1):
				if A[i, j] > A[i, k] + A[k, j]:
					A[i, j] = A[i, k] + A[k, j]
					# print(A[i, j])

	for i in range(no_of_nodes + 1):
		if A[i, i] < 0:
			return None

	return A

def main():
	filename = sys.argv[1]
	no_of_nodes, A = make_graph(filename)
	result = fw(no_of_nodes, A)
	if result is None:
		print('Negative edge cycles!')
	else:
		print(np.amin(result))

if __name__ == '__main__':
	main()

