class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        a=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    a[i][j]=a[i-1][j-1]+1
                else:
                    a[i][j]=max(a[i-1][j],a[i][j-1])
        c=a[m][n]
        return (m-c)+(n-c)