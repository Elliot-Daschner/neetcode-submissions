class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maximum water = min(heights[i], heights[j]) * (j - i)
        i, j = 0, len(heights) - 1
        area = 0
       
        while i < j:
            if (min(heights[i], heights[j]) * (j - i)) > area:
                area = min(heights[i], heights[j]) * (j - i)
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return area
             