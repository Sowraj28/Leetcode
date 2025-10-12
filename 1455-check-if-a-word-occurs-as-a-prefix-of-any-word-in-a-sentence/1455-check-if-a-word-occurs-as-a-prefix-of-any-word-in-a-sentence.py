class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        w=sentence.split()
        n=len(searchWord)
        for i ,j in enumerate(w):
            if j[:n]==searchWord:
                return i+1
        return -1