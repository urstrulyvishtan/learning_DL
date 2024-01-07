class Solution:
    def getSums(self, a: int, b: int) -> int:
        mask = 0xffffffff
        temp = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        if carry != 0:
            return self.getSums(temp, carry)
        return temp if temp <= 0x7fffffff else ~(temp ^ mask)
    