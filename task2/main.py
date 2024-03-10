
def Jacoby(matrix):
    solution = []
    solution.append([0,0,0])
    newRow = []
    i = 1
    paramaterMat = makeSquareMatrix(matrix)
    if checkDominant(paramaterMat) == True:

        while i != 0:
            for j in range(len(paramaterMat)):
                """
                if j == 0:
                     newRow.append((matrix[j][3]-(matrix[j][2]*solution[i-1][2])-(matrix[j][1])*solution[i-1][1])/matrix[j][j])
                if j == 1:
                    newRow.append((matrix[j][3] - (matrix[j][2]*solution[i-1][2]) - (matrix[j][0]*solution[i-1][0])) / matrix[j][j])
                if j == 2:
                    newRow.append((matrix[j][3] - (matrix[j][0]*solution[i-1][0]) - (matrix[j][1]*solution[i-1][1])) / matrix[j][j])
                """
                value = matrix[j][3]
                for k in range(len(paramaterMat)):
                    if k != j:
                        value = value - matrix[j][k]*solution[i-1][k]

                value = value/matrix[j][j]
                newRow.append(value)

            solution.append(newRow)
            newRow = []
            i = i + 1
            if checkStopCondition(solution):
                i = 0

    return solution


def Gauss_seidel(matrix):
    solution = []
    solution.append([0, 0, 0])
    newRow = []
    i = 1
    paramaterMat = makeSquareMatrix(matrix)
    if checkDominant(paramaterMat) == True:

        while i != 0:
            for j in range(len(paramaterMat)):
                """
                if j == 0:
                     newRow.append((matrix[j][3]-(matrix[j][2]*solution[i-1][2])-(matrix[j][1])*solution[i-1][1])/matrix[j][j])
                if j == 1:
                    newRow.append((matrix[j][3] - (matrix[j][2]*solution[i-1][2]) - (matrix[j][0]*solution[i-1][0])) / matrix[j][j])
                if j == 2:
                    newRow.append((matrix[j][3] - (matrix[j][0]*solution[i-1][0]) - (matrix[j][1]*solution[i-1][1])) / matrix[j][j])
                """
                value = matrix[j][3]
                for k in range(len(paramaterMat)):
                    if k != j:
                        if k < j:
                            value = value - matrix[j][k] * newRow[k]
                        else:
                            value = value - matrix[j][k] * solution[i-1][k]

                value = value / matrix[j][j]
                newRow.append(value)

            solution.append(newRow)
            newRow = []
            i = i + 1
            if checkStopCondition(solution):
                i = 0

    return solution


def checkDominant(matrix):
    for i in range(len(matrix)):
        if matrix[i][i]<=0.000001 and matrix[i][i]>=-0.000001:
            print("not dominant")
            return False
    return True


def makeSquareMatrix(matrix):
    newRow = []
    newMatrix = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            newRow.append(matrix[row][col])
        newMatrix.append(newRow)
        newRow = []
    return newMatrix


def checkStopCondition(matrix):
    size = len(matrix)-1
    counter = 0
    for i in range(len(matrix[0])):
        if matrix[size][i]-matrix[size-1][i] <= stopCon and matrix[size][i]-matrix[size-1][i] >= -stopCon:
            counter = counter + 1
    if counter == 3:
        return True
    else:
        return False


stopCon = 0.001

a = ([4,2,0,2],
     [2,10,4,6],
     [0,4,5,5])

JacobyMatrix = Jacoby(a)
print("after ",len(JacobyMatrix)-1," iterations in Jacoby method the solution is:")
print(JacobyMatrix[len(JacobyMatrix)-1])
GaussMatrix = Gauss_seidel(a)
print("after ",len(GaussMatrix)-1," iterations in Gauss seidel method the solution is:")
print(GaussMatrix[len(GaussMatrix)-1])