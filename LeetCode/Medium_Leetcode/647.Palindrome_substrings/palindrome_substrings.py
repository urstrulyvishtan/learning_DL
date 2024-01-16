class Solution:
    def countSubStrings(self, s: str)-> int:
        count = 0
        for i in range(len(s)):
            count += self.expandFromMiddle(s, i, i)
            count += self.expandFromMiddle(s, i, i+1)
        return count
    
    def expandFromMiddle(self, s: str, left: int, right: int)-> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count+=1
            left-=1
            right+=1
        return count