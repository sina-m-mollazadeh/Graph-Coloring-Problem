import time
def StopCondition(elapsed_time,threshold):
    return elapsed_time > threshold

def isColorable(nodes, matrix, index):
    # print("Is Colorable: ",nodes,index)
    # Check if a node can be added to a color group without conflicts
    for node in nodes:
        # print(matrix[node][index],node,index)
        if matrix[node][index] == 1:  # Conflict detected
            return False
    return True


def delayed_print(message, delay=1):
    time.sleep(delay)  
    print(message)


def GenerateNeighbor(index, dict_init, ans, matrix):
    # Remove the node from its current color group
    # print("before",ans)
    for key, values in list(ans.items()):
        if index in values:
            values.remove(index)
    
    # print("after",ans)
    added = False
    ans_pairs = list(ans.items())
    # print("an_pairs",ans_pairs)

    for key_in_dict in range(dict_init + 1, len(ans_pairs)):
        # delayed_print(("key_in_dict",key_in_dict))
        key, value = ans_pairs[key_in_dict]
        # delayed_print(("ans[key]: ",ans[key]))
        if isColorable(ans[key], matrix, index):
            # delayed_print(("possible add",key))
            ans[key].append(index)
            # print(ans)

            dict_init = key
            added = True
            break

    # If the node cannot be added to any existing group, create a new group
    if not added:
        # Try to find the first empty group (if any)
        for i in range(len(ans)):
            if len(ans[i]) == 0:  # Check if the color group is empty
                ans[i].append(index)  # Add to this empty group
                dict_init = i
                added = True
                break
        if not added:
            ans[len(ans)] = [index]
            dict_init = len(ans) - 1


    return ans, dict_init, added

def assign_colors(node_color_dict):
    result = {}
    for color, nodes in node_color_dict.items():
        for node in nodes:  
            result[node] = color
            
    return result


def eval_ans(ans):
    return len({key: val for key, val in ans.items() if val})

def TabuSearch(matrix):
    n = len(matrix)
    s0 = {i: [i] for i in range(n)} 
    begin = time.time()
    end = time.time()
    sBest = s0.copy()
    bestCandidate = s0.copy()
    tabuList = [s0]
    tabuListSize = 5

    while not StopCondition(end - begin,n):
        bestCandidateFitness = n
        for i in range(n):
            dict_init = 0  
            while dict_init < len(s0):
                candidate, dict_init, added = GenerateNeighbor(i, dict_init, s0.copy(), matrix)
                fitness_candidate = eval_ans(candidate)

                if candidate not in tabuList and fitness_candidate < bestCandidateFitness:
                    bestCandidate = candidate
                    bestCandidateFitness = fitness_candidate

                if bestCandidateFitness < eval_ans(sBest):
                    sBest = bestCandidate.copy()

                if bestCandidateFitness == n:
                    break

                tabuList.append(bestCandidate)
                if len(tabuList) > tabuListSize:
                    tabuList.pop(0)
                # delayed_print(("dict_init",dict_init))
            end = time.time()


    return assign_colors(sBest) ,eval_ans(sBest)

