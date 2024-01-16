class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        return max(nums[0], self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))
    def rob_helper(self, nums: list[int])-> int:
        rob1, rob2 = 0,0 
        for i in nums:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    