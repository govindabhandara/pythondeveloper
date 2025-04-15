A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print(result)
# Output: [[10, 10, 10], [10, 10, 10], [10, 10, 10]]