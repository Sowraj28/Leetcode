class Solution:
    def averageValue(self, nums: List[int]) -> int:
        t=0
        c=0
        for i in nums:
            if i%6==0:
                t+=i
                c+=1
        return 0 if c==0 else t//c