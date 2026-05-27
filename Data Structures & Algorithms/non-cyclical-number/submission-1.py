class Solution:
    def isHappy(self, n: int) -> bool:
        digits = str(n)
        seen = set()
        while True:
            count = 0
            for i in digits:
                count += (int(i) ** 2)
            if count == 1:
                return True
            if count in seen:
                return False
            seen.add(count)
            digits = str(count)
            