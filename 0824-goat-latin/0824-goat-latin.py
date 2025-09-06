class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        v=set("aeiouAEIOU")
        res=[]
        w=sentence.split()
        for i,j in enumerate(w,1):
            if j[0] in v:
                a=j+"ma"
            else:
                a=j[1:]+j[0]+"ma"

            a+="a"*i
            res.append(a)
        return " ".join(res)