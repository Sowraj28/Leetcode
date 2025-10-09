class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        a=[0]*n
        c=0
        o=0
        for i in range(n):
            a[i]+=o
            if boxes[i]=="1":
                c+=1
            o+=c
        c=0
        o=0
        for i in range(n-1,-1,-1):
            a[i]+=o
            if boxes[i]=="1":
                c+=1
            o+=c
        return a