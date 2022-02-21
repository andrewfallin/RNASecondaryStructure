# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np

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


def recover():
    print("hi")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    RNA('AACGCGUU')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
