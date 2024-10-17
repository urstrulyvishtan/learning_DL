class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        total_water = 0
        while left<right:
            if height[left]<height[right]:
                if height[left]<left_max:
                    total_water += left_max - height[left]
                else:
                    left_max = height[left]
                left+=1
            else:
                if height[right]<right_max:
                    total_water+=right_max-height[right]
                else:
                    right_max = height[right]
                right-=1
        return total_water       

# if height is empty or has less than 3 elements
# return 0
# left_max max height from 0 to the length
# right_max
# trapped water min(right_max, left_max) - height
# if trapped water >0
# total_water+=watertrapped
# return total _water

# left, right 
# left_max, right_max
# move pointer with smallest heigh towards the other pointer
# if heigh[left] is smaller than height[right]
# move left pointer otherwise right pointer
# calc water trapped at each step by difference between the current max ansd on taht side current heigh

# 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1
# left = 2, right 10
# total_water = 0
# left_max = 1, right_max = 2
# water_trapped = left_max-height[2] = 1

# time complexity O(n)
# space complexity O(1)