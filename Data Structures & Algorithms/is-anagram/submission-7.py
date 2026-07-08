class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=[]
        t=list(t)
        for letter in s:
            if letter in t:
                m.append(letter)
                t.remove(letter)
        if len(m)==len(s):
            return True 
        else:
            return False 
        