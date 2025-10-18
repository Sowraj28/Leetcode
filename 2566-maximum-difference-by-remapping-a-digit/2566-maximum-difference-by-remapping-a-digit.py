class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        for ch in s:
            if ch!='9':
                mx=int(s.replace(ch,'9'))
                break
            else:
                mx=num
        ch=s[0]
        mi=int(s.replace(ch,'0'))
        return mx-mi