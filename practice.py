class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1

# 1, 3, 12, 0, 0
# j= 4
# i = 2

# if no zeroes array remains unchanged
# if all zeroes array remains as is
# empty array remains unchanged

# pointer i to 0, track position of next zero
# iterate array with j
# non zero j swap nums[i]nums[j] i++
# non zero will be at start zeros will be at end

# time complexity O(n)
# space complexity O(1)