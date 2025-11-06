class Solution:
    def removeZeros(self, n: int) -> int:
        a=str(n)
        b=a.replace('0','')
        return int(b) if b else 0