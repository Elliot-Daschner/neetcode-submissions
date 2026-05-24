class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for num in range(1, len(nums)):
            prefix[num] = prefix[num - 1] * nums[num - 1]
        for num in range(len(nums) - 2, -1, -1):
            suffix[num] = suffix[num + 1] * nums[num + 1]
        
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]
        return output