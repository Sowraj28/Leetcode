class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        a={}
        for i in range(lowLimit,highLimit+1):
            s=0
            t=i
            while t>0:
                s+=t%10
                t//=10
            if s in a:
                a[s]+=1
            else:
                a[s]=1
        return max(a.values())
