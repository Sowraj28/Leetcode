class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=Counter(chars)
        t=0
        for i in words:
            w=Counter(i)
            if not(w-c):
                t+=len(i)
        return t
        
        