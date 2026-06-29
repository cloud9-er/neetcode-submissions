class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        one=len(str1)
        two=len(str2)
        value=[]
        if str1 + str2!=str2+str1:
             return ''
        elif one==two:
            return str1
        elif one>two:
            for x in range(1,one+1):
                print(x)
                if one%x==0 and two%x==0:
                    value.append(x)
                    t=max(value)
            return str1[:t]
        elif one<two:
            for i in range(1,two+1):
                if one%i==0 and two%i==0:
                    value.append(i)
                    y=max(value)
            return str2[:y]

        