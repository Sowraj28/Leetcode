class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        a=set()
        for email in emails:
            i,j=email.split("@")
            if '+' in i:
                i=i[:i.index('+')]
            i=i.replace('.','')
            a.add(i+'@'+j)
        return len(a)
