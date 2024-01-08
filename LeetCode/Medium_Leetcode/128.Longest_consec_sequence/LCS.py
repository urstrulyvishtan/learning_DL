class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. Use a set to store all the numbers
        # 2. For each number, check if its left and right neighbors are in the set
        # 3. If so, remove the neighbors from the set and increase the length by 1
        # 4. Return the maximum length
        nums = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 not in nums:
                length = 0
                while num in nums:
                    length += 1
                    num += 1
                max_length = max(max_length, length)
        return max_length