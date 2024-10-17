class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        result = -1
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i]==target:
                count+=1
                if random.randint(1,count) == 1:
                    result = i
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# array might have multiple occurence of same target
# ensure that every valid index has a equal number of probablity of being selected

# when solution object store the array nums
# loop through the array to find all indices where the value equals the target
# for every occurence will use a sampling method to randomly decide to pick the target
# result is index of one of the occurence of the target selected randomly with equal probablity
# 1/count

# nums [1. 2. 3, 3, 3]
# target = 3
# nums = 3 at indices 2, 3, and 4
# index = 2, count = 1
# index = 3, count = 2
# index = 4, count = 3
# Time complexity O(n)
# space complexity O(n)