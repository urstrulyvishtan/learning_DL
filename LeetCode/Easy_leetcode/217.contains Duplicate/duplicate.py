class Solution:
    def duplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))