from collections import defaultdict
import sys
weights={}
weights[('from_node', "to_node")] = 2
print(weights)

edges = defaultdict(list) 
edges["from_node"].append("to_node")
edges["from_node"].append("to_another_node")
edges["from_another_node"].append("to_node")
print(edges["from_node"])