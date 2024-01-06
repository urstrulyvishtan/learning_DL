class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pmap = {} # key: number, value: index

        for i, n in enumerate(nums):
            print(i, n)
            difference = target - n
            print(difference)
            if difference in pmap:
                return [pmap[difference], i]
            pmap[n] = i
            print(pmap)

        return 

if __name__ == "__main__":
    nums = [11,15,2,8,10,7]
    target = 9
    print(Solution().twoSum(nums, target))