class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        maxWater = 0
        l = 0
        r = len(height)-1
        # need to keep track of maximum height on either side because
        # this determines where water is trapped
        leftMax, rightMax = height[l], height[r] 
        while l < r:
            if height[l] < height[r]:
                l+=1
                leftMax = max(leftMax, height[l])
                maxWater += leftMax - height[l] 
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                maxWater += rightMax - height[r]
        return maxWater



