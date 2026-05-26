class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        l, max_len = 0, 0
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1
            cSet.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len


      
        