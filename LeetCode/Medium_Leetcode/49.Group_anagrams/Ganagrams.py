from collections import defaultdict
class Solution:
    def anagrams_group(self, strs: list[str]) -> list[list[str]]:
        values = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            values[tuple(sorted(s))].append(s)
        return values.values()