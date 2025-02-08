import numpy as np
def GenerateGraph(dimensions, density):
    rows = dimensions
    cols = dimensions
    
    random_matrix = np.random.rand(rows, cols)
    upper_triangular_matrix = (random_matrix < density).astype(int)
    
    symmetric_matrix = np.triu(upper_triangular_matrix) + np.triu(upper_triangular_matrix, 1).T
    for i in range(len(symmetric_matrix)):
        for j in range(len(symmetric_matrix)):
            if(i==j):
                symmetric_matrix[i][j]=0
    return symmetric_matrix


def ReturnGraphMatrixForm(dim,density):
    return np.array(GenerateGraph(dim,density))
