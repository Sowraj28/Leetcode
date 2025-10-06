class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        y=[0]*101
        for b,d in logs:
            y[b-1950]+=1
            y[d-1950]-=1
        mx=0
        year=1950
        cu=0
        for i in range(101):
            cu+=y[i]
            if cu>mx:
                mx=cu
                year=1950+i
        return year