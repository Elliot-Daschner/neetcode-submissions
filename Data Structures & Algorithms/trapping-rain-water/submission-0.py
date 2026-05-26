class Solution:
    def trap(self, height: List[int]) -> int:
        pre, suf = [0] * len(height), [0] * len(height)
  

        for i in range(1, len(height)):
            if height[i - 1] > pre[i - 1]:
                pre[i] = height[i - 1]
            else:
                pre[i] = pre[i - 1]
        
        for j in range(len(height) - 2, -1, -1):
            if height[j + 1] > suf[j + 1]:
                suf[j] = height[j + 1]
            else:
                suf[j] = suf[j + 1]
        
        output = 0

        for col in range(len(height)):
            water =  min(pre[col], suf[col]) - height[col]
            if water > 0:
                output += water
        
        return output