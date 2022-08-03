def row_sums(my_matrix: list):
    index = 0
    import numpy as np
    a = np.array(my_matrix)
    res = np.sum(a, axis=1)
    for i in res:
        my_matrix[index].append(i)
        index +=1

    print(my_matrix)
