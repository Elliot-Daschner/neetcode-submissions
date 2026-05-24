class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in s:
            if i not in s_map:
                s_map[i] = 1
            else:
                s_map[i] += 1
        for n in t:
            if n not in t_map:
                t_map[n] = 1
            else:
                t_map[n] +=1
        
        if s_map == t_map:
            return True
        else:
            return False