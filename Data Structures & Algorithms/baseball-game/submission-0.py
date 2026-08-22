class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        score=0
        for i in operations:
            if i=="+":
                stack.append(int(stack[-1])+int(stack[-1-1]))
            elif i=='D':
                stack.append(2*int(stack[-1]))
            elif i=='C':
                stack.pop(-1)
            else:
                stack.append(int(i))
        return sum(stack)
            


        