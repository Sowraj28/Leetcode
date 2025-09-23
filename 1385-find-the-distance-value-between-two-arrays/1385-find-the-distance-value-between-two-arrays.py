class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c=0
        for i in arr1:
            a=True
            for j in arr2:
                if abs(i-j)<=d:
                    a=False

                    break
            if a:
                c+=1
        return c