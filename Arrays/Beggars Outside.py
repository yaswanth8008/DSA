# Problem Description

# There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. 
# When the devotees come to the temple, they donate some amount of coins to these beggars. 
# Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next to each other.

# Given the amount P donated by each devotee to the beggars ranging from L to R index, 
# where 1 <= L <= R <= A, find out the final amount of money in each beggar's pot at the end of the day, 
# provided they don't fill their pots by any other means.
# For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, given by the 2D array B

A = 5 # no.of beggars
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]] # [start,end,value] queries


def each_beggar_got(A,B):
    beggars_amt = [0]*A 
    for i in B:
        start = i[0] - 1
        end = i[1] - 1
        value = i[2]
        beggars_amt[start] += value
        if end != A - 1:
            beggars_amt[end+1] -= value 
    
    for i in range(1,len(beggars_amt)):
        beggars_amt[i] += beggars_amt[i-1] 
    return beggars_amt


print(each_beggar_got(5,[[1, 2, 10], [2, 3, 20], [2, 5, 25]]))
