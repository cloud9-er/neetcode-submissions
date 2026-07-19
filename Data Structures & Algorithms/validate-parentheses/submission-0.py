class Solution:
    def isValid(self, s: str) -> bool:
        st=s[::-1]
        if s==st:
            return True 
        else:
            return False

        