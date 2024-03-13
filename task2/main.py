"""
you can find this git in https://github.com/Babilabong/analiza-nomarit/blob/main/task2/main.py
"""
def Jacoby(matrix):
    solution = []
    solution.append([0,0,0])
    newRow = []
    i = 1
    paramaterMat = makeSquareMatrix(matrix)
    if checkDominant(paramaterMat) == True:

        while i != 0:
            for j in range(len(paramaterMat)):
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
        sum = 0
        for j in range(len(matrix)):
            if i != j:
                sum += abs(matrix[i][j])
        if abs(matrix[i][i]) <= sum:
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

a = ([3,1,1,7],
     [1,3,1,11],
     [1,1,3,7])

JacobyMatrix = Jacoby(a)
print("after ",len(JacobyMatrix)-1," iterations in Jacoby method the solution is:")
print(JacobyMatrix[len(JacobyMatrix)-1])
GaussMatrix = Gauss_seidel(a)
print("after ",len(GaussMatrix)-1," iterations in Gauss seidel method the solution is:")
print(GaussMatrix[len(GaussMatrix)-1])

