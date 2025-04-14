


def selection_sort(A):
    for i in range(len(A)):
        min_value = 1000000
        min_index = -1
        for j in range(i,len(A)):
            if A[j] < min_value:
                min_value = A[j]
                min_index = j 
        A[i],A[min_index] = A[min_index],A[i] 
    return A 


print(selection_sort([-21,23,56,0,5,21,67,54,-12,90]))

