
matrix1=[[45,107],[301,98]]
matrix2=[[12,90], [65,34]]
result=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        result[i][j]=matrix1[i][j]-matrix2[i][j]
print(result)