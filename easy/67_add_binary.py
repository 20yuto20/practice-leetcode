################################################################
# 67. Add Binary
################################################################
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 2進数を10進数に変換
        a_rev = a[::-1]
        b_rev = b[::-1]

        carry = 0
        result = []

        max_len = max(len(a), len(b))

        for i in range(max_len):
            bit_a = int(a_rev[i]) if i < len(a_rev) else 0
            bit_b = int(b_rev[i]) if i < len(b_rev) else 0

            total = bit_a + bit_b + carry

            result_bit = total % 2
            carry = total // 2

            result.append(str(result_bit))

        if carry:
            result.append('1')

        return ''.join(result[::-1])
    
    # OR
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]