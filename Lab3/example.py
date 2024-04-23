
word1 = "BANAN"
word2 = "ANANAS"
n = len(word1)
m = len(word2)
matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]


for i in range(n+1):
    matrix[0][i] = i
for i in range(m+1):
    matrix[i][0] = i
# for

for i in range(1,m+1):
    for j in range(1,n+1):
        if(word1[j-1] == word2[i-1]):
            matrix[i][j] = matrix[i-1][j-1]
        else:
            matrix[i][j] = 1 + min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])

for smol in matrix:
    print(smol)
print(f"Val: {matrix[m][n]}")

