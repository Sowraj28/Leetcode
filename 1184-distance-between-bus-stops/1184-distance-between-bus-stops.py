class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a=start
        b=destination
        if a>b:
            a,b=b,a
        c=sum(distance[a:b])
        t=sum(distance)
        return min(c,t-c)