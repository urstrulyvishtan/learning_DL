class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        count = 0
        for char in s:
            if char == '(':
                count+=1
                result.append(char)
            elif char == ')':
                if count>0:
                    result.append(char)
                    count-=1
            else:
                result.append(char)
            
        fresult = []
        count = 0
        for char in result[::-1]:
            if char == '(' and count == 0:
                continue
            elif char == '(':
                count-=1
                fresult.append(char)
            elif char == ')':
                count+=1
                fresult.append(char)
            else:
                fresult.append(char)
        return ''.join(fresult[::-1])

# traverse the string from left to right:
#   keep count of (
#   for every ) check if matching ( if not mark it for removal

# traverse this string right to left
#   now remove the extra (