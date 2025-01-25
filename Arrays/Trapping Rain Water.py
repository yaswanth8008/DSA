    
# https://leetcode.com/problems/trapping-rain-water/

def trap(height):
    water = 0
    pref_max = [0]*len(height)
    pref_max[0] = height[0]
    for i in range(1,len(height)):
        pref_max[i] = max(pref_max[i-1],height[i])
    suf_max = [0]*len(height)
    suf_max[-1] = height[-1]
    for i in range(len(height)-2,-1,-1):
        suf_max[i] = max(suf_max[i+1],height[i])
    for i in range(1,len(height)-1):
        amt = min(pref_max[i-1],suf_max[i+1]) - height[i]
        if amt > 0:
            water += amt
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))