


https://leetcode.com/problems/add-binary/description/


def addBinary(A, B):
    if len(A) < len(B):
        A = '0'*(len(B) - len(A)) + str(A) 
    elif len(B) < len(A):
        B = '0'*(len(A) - len(B)) + str(B)
   
    binary_string = ''
    cf = 0
    for i in range(len(A)-1,-1,-1):
        summ = int(A[i]) + int(B[i]) + cf
        if summ == 0 or summ == 1:
            cf = 0
            rem = str(summ)
        else:
            cf = int(bin(summ)[2])
            rem = bin(summ)[3]
        binary_string = rem + binary_string 
    if cf == 1:
        binary_string = str(cf) + binary_string 

    return binary_string