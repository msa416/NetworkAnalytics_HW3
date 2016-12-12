# -*- coding: utf-8 -*-
"""
Created on Saturday, December 10

Miram Atie (msa416)

Network Analytics HW2
"""
#import os
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
#cd /Applications/python-louvain-0.3
#python setup.py install
#pip install nose
#python setup.py test
#import sys
#sys.path.append("/Users/Miram/python_louvain.egg-info")
import community
from collections import defaultdict
import random


#os.chdir("/Users/Miram/Desktop/Network Analytics/Assignment 3/1. Network Data/Adjacency Matrices")

#Load the adjacency matrix for village 68
G = np.loadtxt('adj_allVillageRelationships_HH_vilno_68.csv', dtype=int, delimiter=',')
G = np.matrix(G)
G = nx.from_numpy_matrix(G)

#Transform graph to adj list format
#Write to file
nx.write_adjlist(G, "vil_68.adjlist")

#Reread file
G2 = nx.read_adjlist("vil_68.adjlist")

#for line in nx.generate_adjlist(G):
#    print(line)
    
#Look at every node
for (node,adjdict) in G2.adjacency_iter():
    print(node,adjdict)
    
#Detect community structure
partition = community.best_partition(G2)
communities_cnt = len(set(partition.values()))
print(communities_cnt)
pos = nx.spring_layout(G2)
plt.figure(figsize=(10,10))
#plt.axis('off')
values = [partition.get(node) for node in G2.nodes()]
nx.draw_networkx_nodes(G2, pos, node_size=200, cmap=plt.cm.RdYlBu, 
                       node_color=values)

nx.draw_networkx_edges(G2, pos, alpha=0.5)
plt.show()
plt.savefig("community_households.png")

#Bubble chart
#The area of each circle represents the size of each community
bubbles = nx.Graph()
parts=defaultdict(int)
for part in partition.values():
    parts[part] += 1
for part in parts.items():
    bubbles.add_node(part[0], size=part[1])
pos2 = nx.random_layout(bubbles) 
plt.figure(figsize=(5,5))
#plt.axis('off')
nx.draw_networkx_nodes(bubbles, pos2, alpha=0.6, node_size=[x*30 for x in list(parts.values())], 
                       node_color=[random.random() for x in list(parts.values())], 
                                   cmap=plt.cm.RdYlBu)
plt.savefig("community_bubblechart.png")

coms = {}
for com_nbr in set(partition.values()):
    coms[com_nbr] = [nodes for nodes in partition.keys() if partition[nodes] == com_nbr]
print("The best partition found consists of the following communities:\n", coms)

modularity = community.modularity(partition, G2)
print("The modularity of this partition is:", modularity)

print("The size of each community:", parts.values())