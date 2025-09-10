class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m,n=len(strs),len(strs[0])
        c=0
        for i in range(n):
            for j in range(m-1):
                if strs[j][i]>strs[j+1][i]:
                    c+=1
                    break
        return c