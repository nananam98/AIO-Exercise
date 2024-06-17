def levenshtein(source = 'hola', target = 'hello'):
    distances = [[0]*(len(target)+1) for _ in range(len(source)+1)]
    
    for idx in range(len(source)+1):
        distances[idx][0] = idx

    for jdx in range(len(target)+1):
        distances[0][jdx] = jdx

    variable_cost = {'del_cost': 0, 'ins_cost': 0, 'sub_cost': 0}
    for idx in range(1, len(source) + 1):
        for jdx in range(1, len(target) + 1):
            if source[idx-1] == target[jdx-1]:
                distances[idx][jdx] = distances[idx-1][jdx-1]
            else:
                variable_cost['del_cost'] = distances[idx-1][jdx]
                variable_cost['ins_cost'] = distances[idx][jdx-1]
                variable_cost['sub_cost'] = distances[idx-1][jdx-1]

                #Tìm giá key có value nhỏ nhất
                min_key = min(variable_cost, key=variable_cost.get)
                distances[idx][jdx] = variable_cost[min_key] + 1

    print(distances)
    return distances[len(source)][len(target)]

if __name__ == "__main__":
    print(levenshtein())

    