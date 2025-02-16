


# Write a function that takes an integer and returns the number of 1 bits present in its binary representation.

def numSetBits(self, A):
    cnt = 0
    for i in range(32):
        if A >> i & 1 == 1:
            cnt += 1
    return cnt 