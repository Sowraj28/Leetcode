class Solution:
    def reformat(self, s: str) -> str:
        l=[a for a in s if a.isalpha()]
        d=[a for a in s if a.isdigit()]
        if abs(len(l)-len(d))>1:
            return""

        if len(d)>len(l):
            l,d=d,l
        res=[]
        for i in range(len(s)):
            if i%2==0:
                res.append(l.pop())
            else:
                res.append(d.pop())
        return "".join(res)
