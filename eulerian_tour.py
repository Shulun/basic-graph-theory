# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_tour(node, graph, tour):
	for e in graph:
		if node == e[0]:
			graph.remove(e)
			find_tour(e[1], graph, tour)
		elif node == e[1]:
			graph.remove(e)
			find_tour(e[0], graph, tour)
	tour.insert(0, node)

def find_tour_iter(node, graph, tour):
	open_list = [[node, graph]]
	while len(open_list) > 0:
		node_pop, unvisited = open_list.pop()
		tour.insert(0, node_pop)
		if not unvisited:
			return tour
		for edge in unvisited:
			if node_pop in edge:
				next_node = edge[0] if node_pop == edge[1] else edge[1]
				reduced_graph = [e for e in unvisited if e != edge]
				open_list.append([next_node, reduced_graph])

def find_eulerian_tour(graph):
	tour = []
	# find_tour(graph[0][0], graph, tour)
	find_tour_iter(graph[0][0], graph, tour)
	return tour

graph = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 3)]
print(find_eulerian_tour(graph))