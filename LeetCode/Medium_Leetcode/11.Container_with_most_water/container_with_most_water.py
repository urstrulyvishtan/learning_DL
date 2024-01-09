class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            area = min(height[left],height[right]) * (right-left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
    def maxArea2(self, height: list[int]) -> int:
        left = 0
        right =  len(height)-1
        for i in range (len(height)):
            if left<right:
                max_left = max(height[left], height[left+i])
                max_right = max(height[right], height[right-i])
                
        
        return min(max_left, max_right) * ((right-i)-(left+i))
                