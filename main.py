# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
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

'''
Does the comparison to see if there are pairings, 
if there are it returns the max index of the pairing
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

'''
Actually runs the recursion
'''
def RNA_Recursion(i, j, myArray):

    # base case
    if i >= j-4:
        return 0
    else:
        # recurrence relation
        t = get_Pairing(i, j, myArray)
        num1 = RNA_Recursion(i, j - 1, myArray)
        num2 = 1 + RNA_Recursion(i, t-1, myArray) + RNA_Recursion(t+1, j, myArray)
        return max(num1, num2)

'''
Main driver, 
Loops through the array and stores the maximum value returned
NOTE: Can be modified to store values in a Matrix
'''
def RunRNA(myString):
    myArray = list(myString.upper())
    thing = []
    maxVal = 0
    for i in range(len(myArray)):
        for j in range(len(myArray)):
            #thing.append(RNA_Recursion(i, j, myArray))
            myVal = RNA_Recursion(i, j, myArray)
            # Store myVal at the i,j point in the matrix
            if myVal > maxVal:
                maxVal = myVal

    return maxVal

if __name__ == '__main__':
    # RNA('AACGCGUU')
    print(RunRNA('AACGCGUU'))
    print(RunRNA('ggggaaaacccc'))

