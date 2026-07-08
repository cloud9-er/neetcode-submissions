class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=[]
        for letter in s:
            if letter in t:
                m.append(letter)
                if len(m)==len(s):
                    return True 
            else:
                return False 
        