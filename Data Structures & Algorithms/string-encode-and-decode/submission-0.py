class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for word in strs:
            sol = sol + str(len(word)) + "#" + word
        return sol

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            decoded.append(word)
            i = j + 1 + length
        return decoded

            
