class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low<high:
            mid = (low+high)//2
            if nums[mid]>nums[mid+1]:
                high = mid
            else:
                low = mid+1
        return low

# the array may contain one element, it is the peak
# multiple peak elements, any one of the peak
# peak might occur start or end of the array

# low = 0 high = len(nums)-1
# while low<high compute mid = (low+high)//2
#  compare nums[mid] with mid+1
#       if mid>mid+1 set high = mid
#       low = mid+1
# repeat this until low equals to high at which low will be peak

# 1, 2, 3, 1
# low = 0, high = 3
# mid = 1 low = 2
# high = 3
# mid = 2
# high = mid = 2

# time complexity O(log n)
# space complexity O(1)