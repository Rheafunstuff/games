matrix=[[13,25,29,84,97], [78,5,90,76,62]]
print(matrix)
#number of rows
print(len(matrix))
#number of columns
print(len(matrix[1]))
#accessing elements in 2D list
print(matrix[1][2])
print(matrix[0][0])
rows=int(input("enter the number of rows "))
columns=int(input("enter the number of columns "))
matrix=[]
for i in range(rows):
    t=[]
    for j in range(columns):
        element=int(input("enter the element "))
        t.append(element)
    matrix.append(t)
print(matrix)
matrix1=[[26,23], [67,65]]
matrix2=[[54,25], [91,92]]
result=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
print(result)