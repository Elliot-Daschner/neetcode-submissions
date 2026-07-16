class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [0, 1, 2]:
            return n
        
        prev1, prev2 = 2, 1
        result = 0

        for _ in range(n - 2):
            prev1, prev2 = prev1 + prev2, prev1
        
        return prev1

            
