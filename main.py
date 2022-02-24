import numpy as np

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

def RunRNA(myString):
    thing=[]
    myArray = list(myString.upper())
    n = len(myArray)

    OPT = np.zeros((n+1, n+1), dtype= int)

    for k in range(5, n):
        for i in range(1,n-k+1):
            j=i+k
            if i >= j-4:
                OPT[i][j] = 0
            else:
                t = get_Pairing(i-1, j-1, myArray)
                num1 = OPT[i][j - 1]
                num2 = 1 + OPT[i][t - 1] + OPT[t + 1][j - 1]
                # if i <= t and t <= (j-1):
                #     num2 = 1 + OPT[i][t - 1] + OPT[t + 1][j - 1]
                # else:
                #     num2 = 0
                OPT[i][j] = max(num1, num2)
                # store t's here to be space efficient
                OPT[j][i] = t

    # Call recover to print the structure

    # Pseudocode OPT(1,n)
    return OPT[1][n]



def recover():
    print("hi")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Pairs:",RunRNA('AACGCGUU'))
    print("Pairs:",RunRNA('ACCGGUAGU'))
    print("Pairs:",RunRNA('ggggaaaacccc'))
    print("Pairs:", RunRNA('gggggaaaaccccc'))
    print("Pairs:", RunRNA('ggggggaaaacccccc'))
