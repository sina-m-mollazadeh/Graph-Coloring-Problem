import pyomo.environ as pyo
from pyomo.opt import SolverFactory

def ILPModel(matrix,upper):
    nNode = len(matrix)  # Number of nodes

    model = pyo.ConcreteModel()
    
    max_colors = upper

    model.x = pyo.Var(range(nNode), range(max_colors), within=pyo.Binary)  # x[i, j] = 1 if node i uses color j
    model.w = pyo.Var(range(max_colors), within=pyo.Binary)  # w[j] = 1 if color j is used

    # Objective: Minimize the number of colors used
    model.objective = pyo.Objective(expr=sum(model.w[j] for j in range(max_colors)), sense=pyo.minimize)

    # Constraint: Each node must be assigned exactly one color
    model.node_color_constraint = pyo.ConstraintList()
    for i in range(nNode):
        model.node_color_constraint.add(expr=sum(model.x[i, j] for j in range(max_colors)) == 1)

    # # Constraint: If a color is used for any node, w[j] must be 1
    model.color_usage_constraint = pyo.ConstraintList()
    for j in range(max_colors):
        for i in range(nNode):
            model.color_usage_constraint.add(expr=model.x[i, j] <= model.w[j])
    


    # Constraint: Adjacent nodes cannot share the same color
    model.adjacency_constraint = pyo.ConstraintList()
    for i in range(nNode):
        for j in range(i + 1, nNode):
            if matrix[i][j] == 1:  
                for c in range(max_colors):
                    model.adjacency_constraint.add(expr=model.x[i, c] + model.x[j, c] <= 1)





    solver = SolverFactory('glpk') 

    
    result = solver.solve(model,tee=False)
    if result.solver.termination_condition == pyo.TerminationCondition.optimal:
        print(f"Optimal solution found! Within {round(result.Solver.Time*1000)} MiliSeconds")
        color_usage_count = {j: 0 for j in range(max_colors)} 
        print("Node color assignments:")
        for i in range(nNode):
            for j in range(max_colors):
                if pyo.value(model.x[i, j]) > 0:
                    print(f"Node {i} -> Color {j}")
                    color_usage_count[j]+=1
        non_zero_count=sum(1 for count in color_usage_count.values() if count > 0)
        print(pyo.value(model.objective))
    else:
        print("No optimal solution found.")
    return ({i: j for i in range(nNode) for j in range(max_colors) if pyo.value(model.x[i, j]) > 0},pyo.value(model.objective),round(result.Solver.Time))



