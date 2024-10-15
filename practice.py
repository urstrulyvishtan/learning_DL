class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            char = word[index]
            if char == '.':
                for child in node.children:
                    if dfs(index+1, node.children[child]):
                        return True
                return False
            else:
                if char in node.children:
                    return dfs(index+1, node.children[char])
                else:
                    return False
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# init dict class with root node empty trie
# traverse the trie for each char in the word, create new node if it doesn't already exist
# search word : if a char is . : check all possible branches
# otherwise continue the trie traversal

# add bad, b-> creates new node, a, d, dad, pad, mad
# search pad, p doesn't exist so return false..
# search bad, b->a->d word marked return true
# search .ad, .-> all the child nodes, b, d, m. a->d matches for b. return True
# search b.. -> next, try all children of a , and d is found so return True.