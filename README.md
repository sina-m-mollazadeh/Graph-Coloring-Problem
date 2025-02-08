# Graph Coloring Project

This project focuses on solving the graph coloring problem using two approaches:
1. Integer Programming Model
2. Tabu Search Algorithm

## Problem Overview
The graph coloring problem involves assigning colors to the vertices of a graph such that no two adjacent vertices share the same color. The goal is to minimize the number of colors used, known as the chromatic number of the graph.

### Applications
- **Frequency Assignment**: Minimizing interference in Wi-Fi networks.
- **Image Compression**: Grouping color blocks in digital images.
- **Video Synopsis**: Simplifying analysis of surveillance videos.
- **Tumor Segmentation**: Analyzing MRI images for medical diagnosis.
- **Taxi Scheduling**: Allocating distinct time slots for overlapping trips.
- **Timetabling**: Scheduling exams or classes to avoid conflicts.

## Methods Used

### 1. Integer Programming Model
- Formulates the problem as a linear programming model with decision variables and constraints.
- Finds the optimal solution for small graphs.

### 2. Tabu Search Algorithm
- A metaheuristic approach to explore the solution space efficiently.
- Handles large-scale graphs where integer programming is computationally expensive.

## Project Structure
- **main.py**: Core script that generates graphs, computes bounds, and invokes algorithms.
- **model.py**: Implements the integer programming solution.
- **tabu.py**: Contains the tabu search algorithm.
- **plots.py**: Visualizes graphs and results.
- **testCase.py**: Generates graph test cases with varying sizes and densities.

## Output
Results for each graph are stored in the `Plots` directory, containing:
1. Graph before coloring.
2. Graph colored using the tabu search algorithm.
3. Graph colored using the integer programming model.
4. Comparison charts for the number of colors used and time taken.

## Notes
- The integer programming model is suited for small graphs due to computational limits.
- Tabu search is designed for larger graphs and is used to demonstrate scalability.
