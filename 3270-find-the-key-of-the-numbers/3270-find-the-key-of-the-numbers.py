class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1,s2,s3=str(num1),str(num2),str(num3)
        res=""
        b=max(len(s1),len(s2),len(s3))
        s1=s1.zfill(b)
        s2=s2.zfill(b)
        s3=s3.zfill(b)
        for i in range(b):
            res+=str(min(int(s1[i]),int(s2[i]),int(s3[i])))
        return int(res)

