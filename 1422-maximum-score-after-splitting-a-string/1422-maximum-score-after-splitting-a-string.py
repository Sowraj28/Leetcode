class Solution:
    def maxScore(self, s: str) -> int:
        t=s.count('1')
        z,o=0,0
        m=0
        for i in range(len(s)-1):
            if s[i] == '0':
                z+=1
            else:
                o+=1
            sc=z+(t-o)
            m=max(m,sc)
        return m
