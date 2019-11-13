from collections import defaultdict
import sys

edges = defaultdict(list)                              #dictionary of all connected nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}

weights = {}
edges["A"].append("B")
edges["A"].append("C")
edges["C"].append("B")
edges["C"].append("A")
weights[("A", "B")] = 3
"""       
weights[(from_node, to_node)] = weight
self.weights[(to_node, from_node)] = weight"""

print(edges)
print(weights[("A","B")])