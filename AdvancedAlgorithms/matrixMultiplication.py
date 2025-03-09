"""
@description: matrix multiplication program obtained from csv files, using strassens algorithm and textbook algorithm in
order to comparison
"""

import csv

"""
reads and creates the matrix from csv
@param: file path which in this case supposing is in the same directory will be the name of the file
@return: matrix - the array that stores the matrix values
"""
def readMatrix(filePath):
    matrix = []
    with open(filePath, mode = "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Convert each element to an integer or float
            matrix.append([int(element) for element in row])
    return matrix

"""
auxiliary function that allows show in console a given matrix
@param: matrix - the matrix to be shown
"""
def printMatrix(matrix):
    for row in matrix:
        print(row)

"""
auxiliary function to add two matrices
@param: matrixA - first matrix
@param: matrixB - second matrix
"""
def addMatrices(matrixA, matrixB):
    n = len(matrixA)
    return [[matrixA[i][j] + matrixB[i][j] for j in range(n)] for i in range(n)]

"""
auxiliary function to split matrices for strassen's algorithm
@param: matrix - the matrix to be split
"""
def splitMatrix(matrix):
    n = len(matrix)
    mid = n // 2
    A11 = [[matrix[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[matrix[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[matrix[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[matrix[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return A11, A12, A21, A22

"""
auxiliary function to substract two matrices
@param: matrixA - first matrix
@param: matrixB - second matrix
"""
def subtractMatrices(matrixA, matrixB):
    n = len(matrixA)
    return [[matrixA[i][j] - matrixB[i][j] for j in range(n)] for i in range(n)]

"""
matrix multiplication using the textbook algorithm, this considering both are of the same order
@param: matrA - first matrix
@param: matrB - second matrix
@return: resultMatrix - the result matrix of multiplications
@return: noOfMultiplications - total amount of multiplications required to accomplish textbook algorithm
"""
def multiplyMatricesTextbook(matrA, matrB):
    resultMatrix = []
    numRows = len(matrA)
    numCols = len(matrB[0])#aqui es como si metiera a ver cuantos elementos hay en la primera fila
    
    for i in range(numRows):
        resultRow = []
        for j in range(numCols):
            # Calculate the dot product for each element in the result matrix
            dotProduct = sum(matrA[i][k] * matrB[k][j] for k in range(numRows))
            resultRow.append(dotProduct)
        resultMatrix.append(resultRow)

    noOfMultiplications = numRows ** 3
    
    return resultMatrix, noOfMultiplications

"""
matrix multiplication using the Strassen's algorithm, this considering both are of the same order
@param: matrA - first matrix
@param: matrB - second matrix
@return: resultMatrix - the result matrix of multiplications
@return: noOfMultiplications - total amount of multiplications required to accomplish strassen's algorithm
"""
def multiplyMatricesStrassen(matrA, matrB):
    global strassenMultiplicationCount
    n = len(matrA)
    
    if n == 1:  # Base case
        strassenMultiplicationCount += 1
        return [[matrA[0][0] * matrB[0][0]]]
    
    # Partition matrices into submatrices
    A11, A12, A21, A22 = splitMatrix(matrA)
    B11, B12, B21, B22 = splitMatrix(matrB)
    
    # Recursive multiplication
    P1 = multiplyMatricesStrassen(A11, subtractMatrices(B12, B22))
    P2 = multiplyMatricesStrassen(addMatrices(A11, A12), B22)
    P3 = multiplyMatricesStrassen(addMatrices(A21, A22), B11)
    P4 = multiplyMatricesStrassen(A22, subtractMatrices(B21, B11))
    P5 = multiplyMatricesStrassen(addMatrices(A11, A22), addMatrices(B11, B22))
    P6 = multiplyMatricesStrassen(subtractMatrices(A12, A22), addMatrices(B21, B22))
    P7 = multiplyMatricesStrassen(subtractMatrices(A11, A21), addMatrices(B11, B12))
    
    # Combine results to form C
    C11 = addMatrices(subtractMatrices(addMatrices(P5, P4), P2), P6)
    C12 = addMatrices(P1, P2)
    C21 = addMatrices(P3, P4)
    C22 = subtractMatrices(subtractMatrices(addMatrices(P5, P1), P3), P7)
    
    nMatrRes = len(C11)
    return [C11[i] + C12[i] for i in range(nMatrRes)] + [C21[i] + C22[i] for i in range(nMatrRes)]


#obtain the name of files that contains the matrices
print("Please, enter the name of the files containing the square matrices, consider must be in the same folder of the program\nor must provide the relative path to it instead only name")
matrAName = input("Enter the file name of the first matrix: ")
print(matrAName)
matrBName = input("Enter the file name of the second matrix: ")
print(matrBName)

#read the matrices from csv files
matrA = readMatrix(matrAName)
matrB = readMatrix(matrBName)
strassenMultiplicationCount = 0 #set initial count of strassen multiplications to 0

#do the multiplication using text book algorithm
resultTextBookMatrix, textBookMultiplications = multiplyMatricesTextbook(matrA, matrB)

#do the multiplication using strassens algorithm
resultStrassenMatrix = multiplyMatricesStrassen(matrA, matrB)

print("Using text book algorithm resulting matrix: ")
printMatrix(resultTextBookMatrix)
print("\nTotal multiplications required using text book algorithm: ", textBookMultiplications)

print("\n\nUsing Strassen's algorithm resulting matrix: ")
printMatrix(resultStrassenMatrix)
print("\nTotal multiplications required using Strassen's algorithm: ", strassenMultiplicationCount)