class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        real=''
        for letter in s:
            if letter.isalnum():
                real+=letter
        t=''
        for i in reversed(real):
            t+=i
        st=t.strip()
        st=''.join(st)
        print(st)
        if st==real:
            return True
        else:
            return False     