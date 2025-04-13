# Find the Bth smallest element in given array A .

# NOTE: Users should try to solve it in less than equal to B swaps.



# Approach :  Do selection sort till B 
#  In 1 iteration 1 element would be sorted and in B iterations B elements would be sorted



def kthsmallest(A, B):
    A = list(A)
    for i in range(B):
        min_value = 100000000
        min_index = -1
        for j in range(i,len(A)):
            if A[j] <= min_value:
                min_value = A[j]
                min_index = j 
        A[i],A[min_index] = A[min_index],A[i]
    return A[i]


print(kthsmallest([2,1,4,3,2],4))