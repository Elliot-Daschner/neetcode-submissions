class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # idea: use a hashMap and store lists of anagrams as values
        # could use sorted lists as keys?
        ans, output = {}, []
        
        for s in strs:
            if tuple(sorted(s)) in ans:
                ans[tuple(sorted(s))].append(s)
            else:
                ans[tuple(sorted(s))] = [s]

        for key in ans:
            output.append(ans[key])
        
        return output

        
