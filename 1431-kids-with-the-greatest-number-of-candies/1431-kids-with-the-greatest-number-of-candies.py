class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        b=[]
        a=max(candies)
        for i in candies:
            if i+extraCandies>=a:
                b.append(True)
            else:
                b.append(False)
        return b


            
         