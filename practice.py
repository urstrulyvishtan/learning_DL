class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        return cleaned == cleaned[::-1]

# convert string to lower case
# remove all non alpha numeric chars
# reverse the cleaned string
# compare the cleaned string with its reverse

# time complexity : o(n)
# space complexity : O(n)

