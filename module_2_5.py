def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
result1 = get_matrix(1, 2, 3)
result2 = get_matrix(4, 5, 6)
result3 = get_matrix(7, 8, 9)
print(result1)
print(result2)
print(result3)