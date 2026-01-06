class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        a=p.index('*')
        b=p[:a]
        c=p[a+1:]
        i=s.find(b)
        if i==-1:
            return False

        j=s.find(c,i+len(b))
        return j!=-1
