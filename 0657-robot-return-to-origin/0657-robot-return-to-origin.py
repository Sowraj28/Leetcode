class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=Counter(moves)
        if a["L"]==a["R"] and a["U"]==a["D"]:
            return True
        return False
