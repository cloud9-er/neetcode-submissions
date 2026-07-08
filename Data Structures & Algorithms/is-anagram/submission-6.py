class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=[]
        for letter in s:
            if letter in t:
                m.append(letter)
                s.strip(letter)
        if len(m)==len(t):
            return True 
        else:
            return False 
        