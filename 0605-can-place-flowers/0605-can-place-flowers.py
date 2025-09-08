class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m=len(flowerbed)
        for i in range(m):
            if flowerbed[i]==0:
                l=(i==0 or flowerbed[i-1]==0)
                r=(i==m-1 or flowerbed[i+1]==0)
                if l and r:
                    flowerbed[i]=1
                    n-=1
                    if n==0:
                        return True
        return n<=0

    