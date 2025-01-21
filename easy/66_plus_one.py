###############################################################
# 66. Plus One
###############################################################
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        carry = 1

        for i in range(n-1, -1, -1):
            new_val = digits[i] + carry 
            digits[i] = new_val % 10
            carry = new_val // 10

            if carry == 0:
                break
        
        if carry == 1:
            digits.insert(0,1)
        
        return digits