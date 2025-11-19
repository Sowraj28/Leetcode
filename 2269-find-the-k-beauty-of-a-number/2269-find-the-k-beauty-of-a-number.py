class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        c=0
        for i in range(len(s)-k+1):
            sub=int(s[i:i+k])
            if sub!=0 and num%sub==0:
                c+=1
        return c