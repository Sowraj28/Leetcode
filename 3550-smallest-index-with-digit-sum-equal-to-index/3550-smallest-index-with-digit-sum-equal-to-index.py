class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,x in enumerate(nums):
            s=0
            t=x
            while t>0:
                s+=t%10
                t//=10
            if s==i:
                return i
        return -1
