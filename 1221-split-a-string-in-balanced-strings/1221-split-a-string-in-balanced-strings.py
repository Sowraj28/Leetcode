class Solution:
    def balancedStringSplit(self, s: str) -> int:
        b=0
        c=0
        for i in s:
            if i =='L':
                b+=1
            else:
                b-=1
            if b==0:
                c+=1
        return c