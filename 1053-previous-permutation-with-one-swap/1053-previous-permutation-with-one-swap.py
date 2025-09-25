class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        a=arr
        n=len(a)
        i=n-2
        while i>=0 and a[i]<=a[i+1]:
            i-=1
        if i<0:
            return a
        j=n-1
        while a[j]>=a[i] or (j>0 and a[j]==a[j-1]):
            j-=1
        a[i],a[j]=a[j],a[i]
        return a

