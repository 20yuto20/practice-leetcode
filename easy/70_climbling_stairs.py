##############################
# 70. Climbing Stairs
##############################
class Solution:
    def climbStairs(self, n:int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1)]
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    # OR
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp1, dp2 = 1, 2

        for i in range(3, n+1):
            dp3 = dp1 + dp2
            dp1, dp2 = dp2, dp3

        return dp2
    