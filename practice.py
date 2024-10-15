class Solution:
    def isPalindrome(self, s: str) -> bool: # race car
        left, right = 0, len(s)-1 # 0 7
        while left<right:
            while left<right and not s[left].isalnum(): 
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

# convert string to lower case
# remove all non alpha numeric chars
# reverse the cleaned string
# compare the cleaned string with its reverse

# time complexity : o(n)
# space complexity : O(n)

# init left, right
# while left<right skip any non alphanumeric char for both pointers
# compare the char at left and right
# if they match continue inward otherwise return False
# if all valid char match return true

# time complexity O(n)
# space complexity O(1)