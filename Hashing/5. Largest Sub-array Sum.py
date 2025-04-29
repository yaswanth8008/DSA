# Given an array A of N integers.

# Find the largest continuous sequence in a array which sums to zero.



def lszero(self, A):
    d = {}
    pf_arr = [0]*len(A)
    pf_arr[0] = A[0]
    max_length = -10000000
    for i in range(1,len(A)):
        pf_arr[i] = pf_arr[i-1] + A[i]
    for a in range(len(pf_arr)):
        if pf_arr[a] == 0:
            max_length = max(max_length,a+1)
            d[pf_arr[a]] = [a+1,0,a] 

        elif pf_arr[a] not in d:
            d[pf_arr[a]] = [1,a+1] 
        else:
            
            max_length = max(max_length,a - d[pf_arr[a]][1] + 1)
            d[pf_arr[a]][0] = a - d[pf_arr[a]][1] + 1
            d[pf_arr[a]].append(a)
    for i in d:
        if max_length == -10000000:
            return []
        else:
            if d[i][0] == max_length and len(d[i]) != 2:
                return A[d[i][1]:d[i][-1]+1]