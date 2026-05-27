class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp = n * (n + 1) // 2
        return exp - sum(nums)