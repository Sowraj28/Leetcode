class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        o=0
        for i in nums:
            if i%3!=0:
                o+=1
        return o