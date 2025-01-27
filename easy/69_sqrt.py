###################################################################
# 69. Sqrt(x)
###################################################################
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        left = 0
        right = 1
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            sqr = mid * mid

            if sqr == x:
                return mid
            elif sqr < x:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1

        return ans
    