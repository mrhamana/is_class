from math import log2

def maxindex(array):
    
    max_value = float("-inf")
    index = 0
    for i, value in enumerate(array):
        if value > max_value:
            max_value = value
            index = i
    return index

def Entropy(listofoutputs):
    
    n = sum(listofoutputs)
    if n == 0:
        return 0

    e = 0
    for count in listofoutputs:
        if count > 0:
            probability = count / n
            e -= probability * log2(probability)
    return e

def averageEntropy(entropies):
    
    total_count = sum(entry[0] for entry in entropies)
    if total_count == 0:
        return 0

    avg = sum((entry[0] / total_count) * entry[1] for entry in entropies)
    return avg


def changeTable(array, col_number, attribute):
    
    if not array or col_number < 0 or col_number >= len(array[0][1]):
        raise ValueError("Invalid array or column number")

    
    new_header = [col for i, col in enumerate(array[0][1]) if i != col_number]
    newarr = [[array[0][0], new_header]]

    
    for row in array[1:]:
        if row[1][col_number] == attribute:
            filtered_row = [col for i, col in enumerate(row[1]) if i != col_number]
            newarr.append([row[0], filtered_row])

    return newarr




def list_branches(array,column_number): # Tells the types of features there are 
    branch=set()
    for i in range(1,len(array)):
        branch.add(array[i][1][column_number])
        
    return list(branch)

def listoutputs(array):
    
    output_counts = {}

    for row in array[1:]:
        output = row[0]
        output_counts[output] = output_counts.get(output, 0) + 1

    return list(output_counts.values())

def findNODE(array):
    
    if len(array)==1:
        return None
    overall_entropy = Entropy(listoutputs(array))
    if overall_entropy==0:
        return array[1][0]
    IGs = []
    avgs=[]

    for feature_index in range(len(array[0][1])):
        entropies = []

        for branch in list_branches(array, feature_index):
            subset = changeTable(array, feature_index, branch)
            outputs = listoutputs(subset)
            entropy = Entropy(outputs)
            entropies.append([sum(outputs), entropy])

        avg_entropy = averageEntropy(entropies)
        IGs.append(overall_entropy - avg_entropy)
        avgs.append(avg_entropy)
    print("Information Gains:",IGs)
    

    best_feature_index = maxindex(IGs)
    best_feature_name = array[0][1][best_feature_index]

    return [best_feature_name, best_feature_index]
