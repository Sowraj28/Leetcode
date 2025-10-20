class Solution:
    def reorderSpaces(self, text: str) -> str:
        w=text.split()
        a=text.count(' ')
        if len(w)==1:
            return w[0]+' '*a
        
        b=len(w)-1
        c=a//b
        d=a%b
        return (' '*c).join(w)+' '*d