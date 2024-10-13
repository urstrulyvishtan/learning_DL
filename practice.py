class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1  # Pointers to the end of each string
        carry = 0  # Initialize carry
        result = []  # To store the final result in reverse order

        # Add digits from both strings starting from the end
        while i >= 0 or j >= 0 or carry:
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0  # Get digit from num1 or use 0 if i is out of bounds
            digit2 = ord(num2[j]) -ord('0') if j >= 0 else 0  # Get digit from num2 or use 0 if j is out of bounds
            
            total = digit1 + digit2 + carry  # Add digits and carry
            carry = total // 10  # Update carry
            result.append(chr(total%10+ord('0')))  # Append the digit to result
            
            i -= 1  # Move left in num1
            j -= 1  # Move left in num2

        return ''.join(result[::-1])  # Reverse the result list and join to form the final string