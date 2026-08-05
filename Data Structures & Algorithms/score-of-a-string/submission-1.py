class Solution:
    def scoreOfString(self, s: str) -> int:
        res=[]
        for i in range(0,len(s)-1):
            d=abs(ord(s[i])-ord(s[i+1]))
            res.append(d)
        return sum(res)