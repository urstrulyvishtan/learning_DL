class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = result = 0 
        used = {}
        for i, c in enumerate(s):
            if used.get(c, -1) >= start:
                start = used[c]+1
            result = max(result, i-start+1)
            used[c] = i
        return result
    