class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        a={}
        mx=-1
        for i,j in enumerate(s):
            if j in a:
                mx=max(mx,i-a[j]-1)
            else:
                a[j]=i
        return mx