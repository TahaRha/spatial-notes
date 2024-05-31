import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from scipy.stats import norm

class SpaceOSObject:
    def __init__(self, id, position, attributes=None):
        self.id = id
        self.position = np.array(position)
        self.attributes = attributes if attributes else {}

    def distance_to(self, other):
        return euclidean(self.position, other.position)

# Example objects
obj1 = SpaceOSObject(1, [0, 0])
obj2 = SpaceOSObject(2, [3, 4])

print(f"Distance between obj1 and obj2: {obj1.distance_to(obj2)}")

def probabilistic_distance(obj1, obj2, distribution='normal'):
    mean_distance = euclidean(obj1.position, obj2.position)
    if distribution == 'normal':
        dist = norm(mean_distance, 1)
        return dist.rvs()  # Return a sample distance
    else:
        raise ValueError("Unsupported distribution type")

print(f"Probabilistic distance between obj1 and obj2: {probabilistic_distance(obj1, obj2)}")

# Create a graph of SpaceOS objects
G = nx.Graph()
G.add_node(obj1.id, object=obj1)
G.add_node(obj2.id, object=obj2)
G.add_edge(obj1.id, obj2.id, weight=obj1.distance_to(obj2))

# Example shortest path computation
shortest_path = nx.shortest_path(G, source=obj1.id, target=obj2.id, weight='weight')
print(f"Shortest path between obj1 and obj2: {shortest_path}")
