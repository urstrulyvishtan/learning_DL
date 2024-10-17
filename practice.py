class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            balance = 0
            for char in string:
                if char=='(':
                    balance+=1
                elif char==')':
                    balance-=1
                if balance<0:
                    return False
            return balance == 0
        result = []
        visited = set()
        queue = deque([s])
        while queue:
            curr = queue.popleft()
            if isValid(curr):
                result.append(curr)
                found = True
            if found:
                continue
            for i in range(len(curr)):
                if curr[i] not in ('(', ')'):
                    continue
                next_state = curr[:i] + curr[i+1:]
                if next_state not in visites:
                    visited.add(next_state)
                    queue.append(next_state)

        return result if result else [""]
        
        
# s == "" return an empty string
# all valid paranthesis is already valid return as it is
# only letters return string
# )(()
# ((a)b)
# BFS approach
# start checking if the string is valid
#   if valid then add to result and return
#   if not valid, remove one paranthesis and continue checking all possinle results
#   use BFS to ensure to remove no. of paranthesis
# isVaild()
# use set to avoid duplicates 
# use a queue to handle BFS
# once found a level stop further removal

# s = ()())()
# ()()()
# (())()

# time complexity O(n*2^n) O(n)
# space complexity O(n*2^n)