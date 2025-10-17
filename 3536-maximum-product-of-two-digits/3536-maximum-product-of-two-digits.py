class Solution:
    def maxProduct(self, n: int) -> int:
        a=0
        b=0
        while n>0:
            x=n%10
            n=n//10
            if x>a:
                b=a
                a=x
            elif x>b:
                b=x
        return a*b
        