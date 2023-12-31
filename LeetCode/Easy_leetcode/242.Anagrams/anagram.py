class Solution:
    def anagramSorted(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
    

    def AnagramHash( s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_s = {}
        hash_t = {}
        
        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1 # using get method to avoid KeyError
            hash_t[t[i]] = hash_t.get(t[i], 0) + 1

        for key in hash_s:
            if hash_s[key] != hash_t.get(key, 0):
                return False
        return True