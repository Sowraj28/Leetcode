class Solution:
    def average(self, salary: List[int]) -> float:
        a=max(salary)
        b=min(salary)
        salary.remove(a)
        salary.remove(b)
        n=len(salary)
        e=0
        for i in salary:
            e+=i
        return e/n

        