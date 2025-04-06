# There are N players, each with strength A[i]. 
# when player i attack player j, player j strength reduces to max(0, A[j]-A[i]).
# When a player's strength reaches zero, it loses the game, and the game continues in the same manner among other players until only 1 survivor remains.

# Can you tell the minimum health last surviving person can have?


def solve(A):
    def gcd(a,b):
        if b == 0:
            return a 
        else:
            return gcd(b,a%b)
    ans = 0
    for i in range(len(A)):
        ans = gcd(ans,A[i])
    return ans