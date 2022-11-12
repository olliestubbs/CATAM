import numpy as np
import time


# imports the 'numpy' package which gives python the usage of arrays similar to those in MATLAB
def getInverses(prime):
    # function should return an array of inverses
    inverses = np.zeros(prime - 1, dtype=np.int64)
    # initialises array of inverses
    for i in range(1, prime):
        # looping through the integers 1<=i<=p-1
        found = False
        # the 'found' variable ensures that in the case the inverse cannot be found the program
        # returns an error message
        for j in range(1, prime):
            # check, for each j, whether j is the inverse of i
            if i * j % prime == 1:
                inverses[i - 1] = j
                found = True
                break
            else:
                pass
        if found == False:
            return ('Could not find inverses')
        else:
            pass

    return (inverses)


def transpose(i, j, matrix):
    #function to swap to rows in a matrix
    temp = np.array(matrix)
    #define output matrix, using np.array is necessary so that temp is not linked to matrix
    width = matrix.shape[1]
    for x in range(width):
        temp[i, x] = matrix[j, x]
        temp[j, x] = matrix[i, x]
    return temp


def multiply(i, a, matrix, mod):
    #multiply row i by value a and take the modulus
    #use multiply rather than divide as it removes the necessity to find inverses each time this
    #function is called, instead can pass the inverse as an argument
    width = matrix.shape[1]
    for j in range(width):
        matrix[i, j] = (a * matrix[i, j]) % mod
    return matrix

def subtract(i,j,a,matrix,mod):
    width = matrix.shape[1]
    for x in range(width):
        matrix[i,x]=(matrix[i,x]-a*matrix[j,x])%mod
    return matrix
def gaussElim(matrix,mod):
    inverses = getInverses(mod)
    shape = matrix.shape
    currentRow = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            matrix[i,j]=matrix[i,j]%mod
    width = shape[1]
    for x in range(width):
        zeros = True
        main = 0
        for i in range(currentRow,shape[0]):
            if matrix[i,x]!=0:
                zeros =  False
                main = i
                break
        if zeros:
            pass
        else:

            matrix = transpose(currentRow,main,matrix)

            lead = matrix[currentRow,x]

            inverse = inverses[lead-1]

            matrix = multiply(currentRow,inverse,matrix,mod)

            for k in range(currentRow+1,shape[0]):
                lead = matrix[k,x]
                matrix = subtract(k,currentRow,lead,matrix,mod)
            currentRow+=1
    return(matrix)
def findKernel(matrix,mod):
    rowEchelon = gaussElim(matrix,mod)
    basis = []
    l=[]
    shape = rowEchelon.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            if rowEchelon[i,j]!=0:
                l.append(j)
                break
            else:
                pass
    notl = []
    for i in range(shape[1]):
        if i not in l:
            notl.append(i)
    for i in notl:
        vector = np.zeros(shape[1])
        vector[i]=1
        for j in range(len(l)-1,-1,-1):
            rest = 0
            for k in range(l[j]+1,shape[1]):
                rest+=rowEchelon[j,k]*vector[k]
            vector[l[j]]=(-rest)%mod
        basis.append(np.array(vector))
    return basis
def reducedForm(M1,mod):
    result = M1
    shape = M1.shape
    for i in range(1,shape[0]):
        for j in range(shape[1]):
            if M1[i, j] != 0:
                for k in range(i):
                    result = subtract(k,i,result[k,j],M1,mod)
                break
            else:
                pass
    return result



start = time.time()
tester = np.array([[6, 13, 16,18,1]])
B1 = np.array([[4,6,5,2,3,1],[5,0,3,0,1,0],[1,5,7,1,0,12],[5,5,0,3,1,7],[2,1,2,4,0,5]])
B2 = np.array([[3,7,19,3,9,6],[10,2,20,15,3,0],[14,1,3,14,11,3],[26,1,21,6,3,5],[0,1,3,19,0,3]])
A1 = np.array([[0, 1, 7,2,10], [8, 0, 2,5,1], [2, 1, 2,5,5],[7,4,5,3,0]])
A2 = np.array([[6,16,11,14,1,4],[7,9,1,1,21,0],[8,2,9,12,17,7],[2,19,2,19,7,12]])
#print(reducedForm(gaussElim(A1,19),19))
print(gaussElim(A1,19))
#print(findKernel(A1,19))
#print(gaussElim(tester,19))
#print(findKernel(tester,19))
#print(reducedForm(gaussElim(np.array([[1, 1, 0,0,0], [10, 0, 1,0,0], [16,0, 0,1,0],[3,0,0,0,1]]),19),19))
print(gaussElim(np.array([[1, 1, 0,0,0], [10, 0, 1,0,0], [16,0, 0,1,0],[3,0,0,0,1]])))
end = time.time()
print(end-start)

