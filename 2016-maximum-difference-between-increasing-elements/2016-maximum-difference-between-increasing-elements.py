class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn=nums[0]
        md=-1
        for i in range(1,len(nums)):
            if nums[i]>mn:
                md=max(md,nums[i]-mn)
            else:
                mn=nums[i]
        return md

