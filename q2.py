def find_num_of_ones(matrix: [[int]]):
    n, m = len(matrix), len(matrix[0])
    i, j = 0, m-1

    counter = 0
    while i <= n-1 and j >= 0:
        if matrix[i][j] == 1:
            counter += (m-i)
            j -= 1
        else:
            i += 1

    return counter


matrix1 = [[0, 0, 0, 1],
          [0, 0, 1, 1],
          [0, 0, 1, 1],
          [0, 1, 1, 1]]

matrix2 = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]]

matrix3 = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

print(find_num_of_ones(matrix3))