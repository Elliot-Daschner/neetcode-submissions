class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            
        return len(stack) == 0