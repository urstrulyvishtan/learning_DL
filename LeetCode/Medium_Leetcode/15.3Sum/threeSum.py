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
    