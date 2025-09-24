class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s=Counter(arr)
        b=list(s.values())
        return len(b)==len(set(b))