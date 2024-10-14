class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)> len(s):
            return[]
        
        result = []
        sorted_p = sorted(p)

        for i in range(len(s) - len(p) + 1):
            substring = s[i:i+len(p)]
            if sorted(substring) == sorted_p:
                result.append(i)
        return result