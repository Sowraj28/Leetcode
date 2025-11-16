class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        for i in range(low,high+1):
            s=str(i)
            n=len(s)

            if n%2!=0:
                continue
            h=n//2
            l=sum(int(x) for x in s[:h])
            r=sum(int(x) for x in s[h:])

            if l==r:
                c+=1
        return c
