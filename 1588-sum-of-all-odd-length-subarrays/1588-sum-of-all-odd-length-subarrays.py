class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        t=0
        n=len(arr)
        for i in range(n):
            l=i+1
            r=n-i
            ts=l*r
            oc=(ts+1)//2
            t+=oc*arr[i]
        return t