import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
    
def pick_clusters(gn_clusters):
    
    y = [len(cluster) for cluster in gn_clusters]
    x = [n+1 for n in range(len(gn_clusters))]
    
    fig = plt.figure(figsize=(12,10))

    max_cluster_size = [max([len(c) for c in cluster]) for cluster in gn_clusters]
    plt.plot([n+1 for n in range(len(gn_clusters))],max_cluster_size, color=colors[0], label='Max Cluster Size')

    min_cluster_size = [min([len(c) for c in cluster]) for cluster in gn_clusters]
    plt.plot(x,min_cluster_size, color=colors[1], label='Minimum Cluster Size')

    mean_cluster_size = [np.mean([len(c) for c in cluster]) for cluster in gn_clusters]
    plt.plot(x,mean_cluster_size, color=colors[2], label='Mean Cluster Size')

    median_cluster_size = [np.median([len(c) for c in cluster]) for cluster in gn_clusters]
    plt.plot(x,median_cluster_size, color=colors[3], label='Median Cluster Size')

    single_node_clusters = [sum([1 if len(c)==1 else 0 for c in cluster]) for cluster in gn_clusters]
    plt.plot(x,single_node_clusters, color=colors[6], label='Number of Single Node Clusters')

    small_clusters = [sum([1 if len(c)<=5 else 0 for c in cluster ]) for cluster in gn_clusters]
    plt.plot(x,small_clusters, color=colors[5], label='Number of Small Clusters (5 or less nodes)')

    plt.legend(loc=(1.01,.75), fontsize=14)
    plt.title('Cluster Size Metrics versus Number of Edges Removed', fontsize=14)
    plt.xlabel('Number of Edges Removed', fontsize=14)
    plt.ylabel('Cluster Metric')
    plt.ylim(0,80)
    plt.yticks(ticks=list(range(0,80,5)))
    plt.show()