import sys

# class Node:
# 	def __init__(self, id):
# 		self.id = id
# 		self.incoming_nodes = {}
# 		self.outgoing_nodes = {}

# 	def add_incoming_node(self, inc, weight):
# 		self.incoming_nodes[inc] = weight

# 	def add_outgoing_node(self, out, weight):
# 		self.outgoing_nodes[out] = weight

# 	def __str__(self):
# 		# use backslash to continue defining string in next line
# 		message = 'Node: ' + str(self.id) + ' Incoming nodes: ' + \
# 		str([node.id for node in self.incoming_nodes]) + ' Outgoing nodes: ' + str([node.id for node in self.outgoing_nodes])
# 		return message

class Graph:
	def __init__(self):
		self.edges = []

	def add_edge(self, u, v, w):
		self.edges.append((u, v, w))

	def __str__(self):
		return 'Edges: {}'.format(self.edges)

def make_graph(filename):
	G = Graph()
	with open(filename, 'r') as f:
		lines = f.readlines()
		line_0 = lines[0].strip('\n').split(' ')
		no_of_nodes = int(line_0[0])
		for line in lines[1: ]:
			l = line.strip('\n').split(' ')
			G.add_edge(int(l[0]), int(l[1]), int(l[2]))

	return no_of_nodes, G

def bf_algorithm(G, no_of_nodes, source):
	distance = {}
	for i in range(1, no_of_nodes + 1):
		distance[i] = float('Inf')
	distance[source] = 0

	for itr in range(no_of_nodes):
		for (u, v, w) in G.edges:
			temp_dist = distance[u] + w
			# print(temp_dist, distance[v])
			if temp_dist < distance[v]:
				distance[v] = temp_dist

	for (u, v, w) in G.edges:
		if distance[u] + w < distance[v]:
			# print('Negative edge cycles!')
			return None

	return distance

def bf_loop(G, no_of_nodes):
	all_distances = []
	for i in range(1, no_of_nodes + 1):
		distance = bf_algorithm(G, no_of_nodes, i)
		if distance is None:
			return None
		all_distances.extend([distance[node] for node in distance])
	return all_distances

def main():
	filename = sys.argv[1]
	no_of_nodes, G = make_graph(filename)
	result = bf_loop(G, no_of_nodes)
	if result is None:
		print('Negative edge cycles!')
	else:
		print(min(result))

if __name__ == '__main__':
	main()



