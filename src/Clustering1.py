from . import graph as gr
from . import plot_clustered_graph as pg
import networkx as nx
from community import community_louvain
import pandas as pd
import numpy as np

def community_detect(time_lower,time_upper):
  edgedata=gr.graphformation(time_lower,time_upper)[0]
  edge_data = pd.DataFrame(edgedata, columns=["node1", "node2","weight"])
  g = nx.Graph()
  g = nx.from_pandas_edgelist(edge_data, source='node1', target='node2', edge_attr ='weight',)
  partition = community_louvain.best_partition(g)
  print(partition)
  pg.plotgraph(partition,g)
  return partition