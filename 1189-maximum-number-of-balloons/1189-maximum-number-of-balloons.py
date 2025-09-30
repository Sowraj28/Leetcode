class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c=Counter(text)
        r={'b':1,'a':1,'l':2,'o':2,'n':1}
        return min(c[ch]//r[ch] for ch in r)