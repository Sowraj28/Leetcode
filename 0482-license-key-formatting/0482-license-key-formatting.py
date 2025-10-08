class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        a=[]
        c=0
        for i in reversed(s):
            if i=="-":
                continue
            a.append(i.upper())
            c+=1

            if c == k:
                a.append("-")
                c=0
        if a and a[-1]=="-":
            a.pop()
        return ''.join(reversed(a))