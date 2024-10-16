class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool: # hello, leetcode
        alien_dict = {char: index for index, char in enumerate(order)}
    
        # Step 2: Compare each pair of adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # Step 3: Compare the words character by character
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    # If characters are different, check their order in alien_dict
                    if alien_dict[word1[j]] > alien_dict[word2[j]]:
                        return False  # If the first word comes after the second, not sorted
                    # If we find the first different character and it's in the right order, move to the next pair of words
                    break
            else:
                # If we finished the loop and all characters were the same, the shorter word should come first
                if len(word1) > len(word2):
                    return False
        
        # If all word pairs are sorted according to alien_dict, return True
        return True

# create dict map each char in order to its idx
# loop adjacent pair each words:
#   compare the words char by char using the dict
#   if one word is a prefix of another, then shorter one must come first
# if all comparisons are valid then return True, otherwise it will be False