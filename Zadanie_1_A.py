'''
Create 2 matrixes using A and B
𝑨 = [−2 5 5 0 4
    5 −4 −4 5 4
    1 −5 −4 3 2 ]
𝑩 = [0 0 3 4 4
2 −2 5 1 2
2 −4 2 −2 −3 ]
'''
A = [[-2, 5, 5, 0, 4], [5, -4, -4, 5, 4], [1, -5, -4, 3, 2]]
B = [[0, 0, 3, 4, 4], [2, -2, 5, 1, 2], [2, -4, 2, -2, -3]]

# Create a matrix C = A + B
C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Print the matrix C
print(C)