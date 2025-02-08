from testCase import ReturnGraphMatrixForm
from model import ILPModel
from plot import PlotColoredGraph,plot_results
from tabu import TabuSearch
import matplotlib.pyplot as plt
import numpy as np
import time
import os
# print("*"*10,"Please Type The Dimentions of Graph and its Density in the below Format 20 0.5 : ","*"*10)
# dim,density=map(float,input("Please Type The Corresponding Number: ").split(' '))
graph_list=[(10,0.1),(10,0.2),(10,0.3),(10,0.4),(10,0.5),(20,0.1),(20,0.2),(20,0.3)]
def Iterate(list_item):
    dim, density = list_item
    matrix = ReturnGraphMatrixForm(dim=int(dim), density=density)


    degrees = np.sum(matrix, axis=1)
    begin_bound=time.time()
    upper = int(max(degrees)+1)
    


    end_bound=time.time()
    bound_time=end_bound-begin_bound
    print(f"Upper bound found within {round(bound_time,2)*1000} Miliseconds")
    nNode = len(matrix)
    default_colors = {i: 0 for i in range(nNode)}
    os.makedirs("Plots",exist_ok=True)
    # Generate a valid directory path
    path = f"Plots/Graph_With_{int(dim)}_{density}".replace("*", "_").replace(" ", "_")
    
    # Create the directory if it doesn't exist
    os.makedirs(path, exist_ok=True)
    
    # Save the pre-colored graph
    PlotColoredGraph(matrix, default_colors, os.path.join(path, f'Pre_colored_{int(dim)}_{density}'))
    # ILP Model
    node_colors_ILP, num_colors_used_ILP, time_ILP = ILPModel(matrix,upper)
    PlotColoredGraph(matrix, node_colors_ILP, os.path.join(path, f'ILP_{int(dim)}_{density}'))
    
    # Tabu Search
    begin = time.time()
    node_colors_tabu, num_colors_used_tabu = TabuSearch(matrix)
    end = time.time()
    PlotColoredGraph(matrix, node_colors_tabu, os.path.join(path, f'Tabu_{int(dim)}_{density}'))
    
    

    methods = ['ILP', 'Tabu Search']
    num_colors_used = [num_colors_used_ILP, num_colors_used_tabu]
    time_taken = [time_ILP, round((end - begin+bound_time), 2)]

    x = range(len(methods))

    fig, ax1 = plt.subplots()
    bar_width = 0.35
    ax1.bar(x, num_colors_used, width=bar_width, label='Number of Colors Used', color='blue', alpha=0.7)

    ax2 = ax1.twinx()
    ax2.bar([p + bar_width for p in x], time_taken, width=bar_width, label='Time Taken (s)', color='orange', alpha=0.7)

    ax1.set_xlabel('Method')
    ax1.set_ylabel('Number of Colors Used', color='blue')
    ax2.set_ylabel('Time Taken (s)', color='orange')
    ax1.set_xticks([p + bar_width / 2 for p in x])
    ax1.set_xticklabels(methods)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.title('Comparison of ILP and Tabu Search')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig(os.path.join(path, f'Comparison_ILP_{int(dim)}_{density}.jpg'))

    with open(os.path.join(path, 'outputs.txt'), 'w') as f:
        f.write(f"ILP Node Colors: {node_colors_ILP}\n")
        f.write(f"Tabu Node Colors: {node_colors_tabu}\n")
        f.write(f"{int(dim)},{density},{num_colors_used},{time_taken}")
    return num_colors_used, time_taken,[dim,density]

answers=[]
while len(graph_list)!=0:
    answers.append(Iterate(graph_list[-1]))
    graph_list.pop()
    print(answers[-1])

plot_results(answers=answers)
with open(f'all_outputs.txt', 'w') as f:
    for ans in answers:
        f.write(f"{ans}\n")