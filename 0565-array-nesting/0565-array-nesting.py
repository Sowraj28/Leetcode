class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
            mx=0
            for i in range(len(nums)):
                c=0
                while nums[i]!=-1:
                    a=nums[i]
                    nums[i]=-1
                    i=a
                    c+=1
                mx=max(mx,c)
            return mx