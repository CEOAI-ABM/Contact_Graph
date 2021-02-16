import networkx as nx 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd

def plt_graph(partition,edgedata):
  
  edge_data = pd.DataFrame(edgedata, columns=["node1", "node2","weight"])
  g = nx.Graph()
  g = nx.from_pandas_edgelist(edge_data, source='node1', target='node2', edge_attr ='weight',)
  # visualization
  plt.figure(figsize=(20,16))
  plt.grid(False)
  pos=nx.spring_layout(g)
  cmap = cm.get_cmap('plasma', max(partition.values()) + 1)
  nx.draw_networkx_nodes(g, pos, partition.keys(), node_size=50,cmap=cmap, node_color=list(partition.values()))
  nx.draw_networkx_edges(g, pos, alpha=0.5)
  plt.savefig("clustered_graph_spring_layout.png")
