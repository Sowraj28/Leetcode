class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=list(zip(heights,names))
        a.sort(reverse=True)
        return [name for _, name in a]