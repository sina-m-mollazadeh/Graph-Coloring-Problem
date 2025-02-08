import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import os
import random
colors = list(matplotlib.colors.CSS4_COLORS.keys())
random.shuffle(colors)
color_map={}
for i in range(len(colors)):
    color_map[i]=colors[i]

# color_map = {
#     0: "red",
#     1: "blue",
#     2: "green",
#     3: "yellow",
#     4: "purple",
#     5: "orange",
#     6: "pink",
#     7: "brown",
#     8: "cyan",
#     9: "magenta",
#     10: "lime",
#     11: "teal",
#     12: "navy",
#     13: "maroon",
#     14: "olive",
#     15: "gray",
#     16: "gold",
#     17: "silver",
#     18: "black",
#     19: "indigo",
#     20: "violet",
#     21: "beige",
#     22: "coral",
#     23: "emerald",
#     24: "mint",
#     25: "turquoise",
#     26: "lavender",
#     27: "olive drab",
#     28: "plum",
#     29: "salmon",
#     30: "marigold",
#     31: "lavender blush",
#     32: "orchid",
#     33: "periwinkle",
#     34: "sage",
#     35: "seafoam",
#     36: "sky blue",
#     37: "teal green",
#     38: "fuchsia",
#     39: "amber",
#     40: "rosewood",
#     41: "charcoal",
#     42: "khaki",
#     43: "wheat",
#     44: "platinum",
#     45: "mint green",
#     46: "lemon",
#     47: "peach",
#     48: "cerulean",
#     49: "maroon red"
# }

def PlotColoredGraph(matrix, node_colors, output_path):
    nNode = len(matrix)

    node_color_names = [
        color_map.get(node_colors[i], "gray") for i in range(len(node_colors))
    ]    

    G = nx.Graph()
    G.add_nodes_from(range(nNode))
    for i in range(nNode):
        for j in range(i + 1, nNode):
            if matrix[i][j] == 1:
                G.add_edge(i, j)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_color_names, 
        node_size=500,
        edge_color="gray",
        font_size=10,
        font_weight="bold",
    )
    plt.title("Colored Graph Representation")

    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    plt.savefig(f"{output_path}.jpg")
    plt.close()

import matplotlib.pyplot as plt
import numpy as np


def plot_results(answers):
    dims_densities = [f"{dim} ({density})" for _, _, (dim, density) in answers]
    num_colors_ILP = [num_colors[0] for num_colors, _, _ in answers]
    num_colors_tabu = [num_colors[1] for num_colors, _, _ in answers]
    time_ILP = [times[0] for _, times, _ in answers]
    time_tabu = [times[1] for _, times, _ in answers]

    x = np.arange(len(dims_densities)) 
    bar_width = 0.35
    plt.figure(figsize=(10, 6))
    plt.bar(x - bar_width / 2, num_colors_ILP, bar_width, label="ILP", color="blue", alpha=0.7)
    plt.bar(x + bar_width / 2, num_colors_tabu, bar_width, label="Tabu Search", color="orange", alpha=0.7)
    plt.xticks(x, dims_densities, rotation=45, ha="right")
    plt.xlabel("Graph (dim, density)")
    plt.ylabel("Number of Colors Used")
    plt.title("Number of Colors Used by ILP vs Tabu Search")
    plt.legend()
    plt.tight_layout()
    plt.savefig("Plots/number_of_colors_comparison.jpg")

    plt.figure(figsize=(10, 6))
    plt.plot(dims_densities, time_ILP, label="ILP", marker="o", color="blue", linewidth=2)
    plt.plot(dims_densities, time_tabu, label="Tabu Search", marker="s", color="orange", linewidth=2)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Graph (dim, density)")
    plt.ylabel("Time Taken (s)")
    plt.title("Time Taken by ILP vs Tabu Search")
    plt.legend()
    plt.tight_layout()
    plt.savefig("Plots/time_taken_comparison.jpg")

    plt.figure(figsize=(10, 6))
    plt.scatter(num_colors_ILP, time_ILP, label="ILP", color="blue", marker="o", s=100, alpha=0.7)
    plt.scatter(num_colors_tabu, time_tabu, label="Tabu Search", color="orange", marker="s", s=100, alpha=0.7)
    plt.xlabel("Number of Colors Used")
    plt.ylabel("Time Taken (s)")
    plt.title("Tradeoff: Number of Colors Used vs. Time Taken")
    plt.legend()
    plt.grid(alpha=0.5)
    plt.tight_layout()
    plt.savefig("Plots/tradeoff_colors_vs_time.jpg")





