# Program to add two 2x2 matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]

print("Resultant Matrix:")
for row in result:
    print(row)