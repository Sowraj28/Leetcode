class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=Counter(p)
        b=Counter()
        res=[]
        k=len(p)
        for i,char in enumerate(s):
            b[char]+=1
            if i>=k:
                c=s[i-k]
                b[c]-=1
                if b[c]==0:
                    del b[c]
            if b==a:
                res.append(i-k+1)
        return res

