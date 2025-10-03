class Solution:
    def sortSentence(self, s: str) -> str:
        w=s.split()
        n=len(w)
        res=[""]*n
        for i in w:
            p=int(i[-1])-1
            res[p]=i[:-1]
        return " ".join(res)