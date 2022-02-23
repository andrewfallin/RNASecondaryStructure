# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
'''
import numPy as np
def RNA(b_string):
    #convert b_string to array of b1 to bn {AUCG} characters
    b_arr=list(b_string)
    n = len(b_arr)
    if {b_arr[1], b_arr[7]} == ({'A', 'U'}):
        print("works")
    #create matrix to store subproblem solutions
    M = np.zeros((n,n),dtype=int)
    print(f'{np.array(M)}')
    #Initialize M(i,j)=0 whenever i >= j-4
    for k in range(5, n):
        for i in range (1,k):
            j=i+k
            if i >= (j-4):
                M[i,j] = 0
            #check if b_j is involved in a pair
            #if (b_arr[i] == 'A' && b_arr[j] == 'C') || (b_arr[i] == 'C' && b_arr[j] == 'A') || (b_arr[i] == 'U' && b_arr[j] == 'C') || (b_arr[i] == 'A' && b_arr[j] == 'C'):
            #M(i,j)=
    return M[1,n]
'''
def get_Pairing(i, j, myArray):

    j_Char = myArray[j]
    maxT = i
    for t in range(i, j-1):
        t_Char = myArray[t]
        if j_Char == 'A' and t_Char == 'U':
            maxT = t
        elif j_Char == 'C' and t_Char == 'G':
            maxT = t
        elif j_Char == 'U' and t_Char == 'A':
            maxT = t
        elif j_Char == 'G' and t_Char == 'C':
            maxT = t
    return maxT

def RNA_Recursion(i, j, myArray):

    if i >= j-4:
        return 0
    else:
        t = get_Pairing(i, j, myArray)
        num1 = RNA_Recursion(i, j - 1, myArray)
        num2 = 1 + RNA_Recursion(i, t-1, myArray) + RNA_Recursion(t+1, j, myArray)
        return max(num1, num2)


def RunRNA(myString):
    myArray = list(myString.upper())
    OPT = np.empty((len(myArray),len(myArray)))
    for i in range(len(myArray)):
        for j in range(len(myArray)):
            #thing.append(RNA_Recursion(i, j, myArray))
            OPT[i][j] = RNA_Recursion(i, j, myArray)

    #store t's here to be space efficient
    for i in range(len(myArray)):
        for j in range(0,i):
            OPT[i][j] = OPT[j][i]

    # Pseudocode OPT(1,n)
    return OPT[0][len(myArray)-1]


def recover():
    print("hi")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # RNA('AACGCGUU')
    print(RunRNA('AACGCGUU'))
    print(RunRNA('ggggaaaacccc'))
    print(RunRNA('gggggaaaaccccc'))
    print(RunRNA('acaugauggccaugu'))
    print(RunRNA('cagaucggcgauacgagcauagcaaugcuaagcgagcuuagcugca'))
