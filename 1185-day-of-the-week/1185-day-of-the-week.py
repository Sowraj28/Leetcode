class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        y=year
        if month<3:
            y-=1
        w=(y+y//4-y//100+y//400+t[month-1]+day)%7
        return days[w]
        