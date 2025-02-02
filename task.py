# # 1. Diagonal elements sum (Level 1 is any one diagonal and level 2 is )


# mat = [[1,  2,  3,  4],
#        [5,  6,  7,  8],
#        [9, 10, 11, 12],
#        [13,14, 15, 16]]

# mat = [[1, 2],
#        [3, 4]]

# mat = [[5]]

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

rowlen = len(mat)
collen = len(mat[0])

firstdiagonal = 0
seconddiagonal=0

if rowlen == collen:
    k=rowlen-1
    for i in range(rowlen):  
        firstdiagonal += mat[i][i] 
        seconddiagonal+=mat[i][k]
        k-=1
totaldiagonal=firstdiagonal+seconddiagonal
if rowlen%2==1:
    totaldiagonal-=mat[rowlen//2][rowlen//2]
print(firstdiagonal)
print(seconddiagonal)
print(totaldiagonal)


# 2. Add 2 matrixes


# mat1=[[1,2,3],
#       [4,5,6],
#       [7,8,9]]
# mat2=[[9,8,7],
#       [6,5,4],
#       [3,2,1]]

mat1 = [[1, 2, 3],
        [4, 5, 6]]

mat2 = [[6, 5, 4],
        [3, 2, 1]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat1[i][j]=mat1[i][j]+mat2[i][j]
print(mat1)