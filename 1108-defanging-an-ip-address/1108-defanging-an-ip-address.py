class Solution:
    def defangIPaddr(self, address: str) -> str:
        a="[.]"
        b=""
        for i in address:
            if i ==".":
                b+=a
            else:
                b+=i
        return b

