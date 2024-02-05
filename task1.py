"""
input 2 square matrix and choose:
1 for print the adding
2 for print the mul
3 for printing our input
4 to choose again 2 matrix
5 to exit the program

you can find this code in the git:
https://github.com/Babilabong/analiza-nomarit

"""
def sumMatrix(mat1,mat2,size):
    newMatrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(mat1[i][j] + mat2[i][j])
        newMatrix.append(row)
    return newMatrix

def mulMatrix(mat1,mat2,size):
    newMatrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0.00)
        newMatrix.append(row)

    for i in range(size):
        for j in range(size):
            for k in range(size):
                newMatrix[i][j] += mat1[i][k] * mat2[k][j]
    return newMatrix

def printMatrix(mat,size):
    for i in range(size):
        print("[",end=" ")
        for j in range(size):
            print(mat[i][j],end=" ")
        print("]")


flag1 = True
while(flag1):
    flag2 = True
    mat1 = []
    mat2 = []
    size = int(input("please enter the size of the matrix: "))
    for i in range(size):
        row = []
        for j in range(size):
            row.append(float(input("please enter the number in the " + str(i+1) + "x" + str(j+1) + " spot in matrix 1: ")))
        mat1.append(row)
    for i in range(size):
        row = []
        for j in range(size):
            row.append(float(input("please enter the number in the " + str(i+1) + "x" + str(j+1) + " spot in matrix 2: ")))
        mat2.append(row)
    while(flag2):
        choice = int(input("please enter\n1 for adding\n2 for multiplication\n3 for printing the matrix that you entered\n4 for choosing the matrixs again\n5 for exit the program\n"))
        if choice == 1:
            printMatrix(sumMatrix(mat1,mat2,size),size)
            print("\n")
        elif choice == 2:
            printMatrix(mulMatrix(mat1,mat2,size),size)
            print("\n")
        elif choice == 3:
            printMatrix(mat1,size)
            print("\n")
            printMatrix(mat2,size)
            print("\n")
        elif choice == 4:
            flag2 = False
        elif choice == 5:
            flag1 = False
            flag2 = False
        else:
            print("invalid try again")