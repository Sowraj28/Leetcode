class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            if i=="#":
                if a:
                    a.pop()
            else:
                a.append(i)
        for j in t:
            if j=="#":
                if b:
                    b.pop()
            else:
                b.append(j)
        return a==b
