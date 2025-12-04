class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ms=0
        c=1
        i=0
        n=len(arr)
        
        while True:
            if i<n and arr[i]==c:
                i+=1
            else:
                ms+=1
                if ms==k:
                    return c
            c+=1
