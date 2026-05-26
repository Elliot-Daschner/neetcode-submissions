class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, maxL, maxCount = 0, 0, 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxCount = max(maxCount, freq[s[r]])
            while (r - l + 1 - maxCount) > k:
                freq[s[l]] -= 1
                l += 1
            
            maxL = max(maxL, r - l + 1)
        
        return maxL