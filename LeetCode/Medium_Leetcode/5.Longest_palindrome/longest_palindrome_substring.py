class Solution:
    def longestPalindrome(self, s: str)-> str:
        if len(s) == 0:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandFromMiddle(s, i, i)
            len2 = self.expandFromMiddle(s, i, i+1)
            length = max(len1, len2)
            if length > end - start:
                start = i - ((length - 1)//2)
                end = i + (length//2)
        return s[start:end+1]
    
    def expandFromMiddle(self, s: str, left: int, right: int)-> int:
        if len(s) == 0 or left > right:
            return 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return right - left - 1