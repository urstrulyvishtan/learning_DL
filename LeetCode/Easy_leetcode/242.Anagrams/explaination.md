Anagram is finding if same characters are present in the other string

basically working of python Counter()

there are two possible solutions
Sorting:
Time Complexity: O(nlogn)
Space Complexity: O(S+T)

we will sort both strings and compare. Simple!

HashMap:
Time Complexity: O(S+T)
Space Complexity: O(S+T)

we have to create two hash maps, count each character and save it in respective maps

then we can compare and return result