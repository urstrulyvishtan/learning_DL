class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool: # 23, 2, 4, 6, 7 k = 6
        remainder = {0:-1} 
        cumulative_sum = 0
        for i in range(len(nums)): #23. 2
            cumulative_sum+=nums[i] #0+23 23+2
            if k!=0:
                cumulative_sum%=k #23%6 = 5 25%6 = 1
            if cumulative_sum in remainder: # 
                if i-remainder[cumulative_sum]>1: #
                    return True #
            else:
                remainder[cumulative_sum] = i # 0:-1, 5:0, 1:1
        return False  
        
# init remainder to store the remainders of cumulative sum 
# for each element compute sum/k
# if the remainder has seen before map: check if the subarray formed between prev remainder and current index len atleast 2
# if so return True
# store the remainder with current index in the map
# if no subarray is found return False

# time complexity O(n)
# space complexity O(min(n, k))