class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        a=set()
        for i,j in ranges:
            for b in range(i,j+1):
                a.add(b)
        for i in range(left,right+1):
            if i not in a:
                return False
        return True