class Solution:
    def scoreOfString(self, s: str) -> int:
        lst=[]
        score=[ord(i) for i in s]
        for t in range(len(score)-1):
            l=abs(score[t]-score[t+1])
            lst.append(l)
        return sum(lst)