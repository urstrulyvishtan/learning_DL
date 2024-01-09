class Solution:
    def Sum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum == 0:
                        res.append([nums[i],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum < 0:
                        left += 1
                    else:
                        right -= 1
        return res
    
    def sum2(self, nums: list[int]) -> list(list[int]):
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1