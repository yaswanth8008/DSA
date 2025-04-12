# In the classic problem of the Towers of Hanoi, you have 3 towers numbered from 1 to 3 (left to right) 
# and A disks numbered from 1 to A (top to bottom) of different sizes which can slide onto any tower.
# The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).
# You have the following constraints:

# Only one disk can be moved at a time.
# A disk is slid off the top of one tower onto another tower.
# A disk cannot be placed on top of a smaller disk.

# You have to find the solution to the Tower of Hanoi problem.
# You have to return a 2D array of dimensions M x 3, where M is the minimum number of moves needed to solve the problem.
# In each row, there should be 3 integers (disk, start, end), where:

# disk - number of the disk being moved
# start - number of the tower from which the disk is being moved
# end - number of the tower to which the disk is being moved

def towerOfHanoi(A):
    ans = []
    def TOH(n,source,destination,helper):
        if n == 0:
            return None
        TOH(n-1,source,helper,destination)
        ans.append([n,source,destination])
        TOH(n-1,helper,destination,source)
    source = 1
    destination = 3
    helper = 2
    n = A
    TOH(n,source,destination,helper)
    return ans