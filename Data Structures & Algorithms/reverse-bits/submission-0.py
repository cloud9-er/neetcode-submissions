class Solution:
    def reverseBits(self, n: int) -> int:
        result=[]
        for i in range(32):
            v=n%2
            result.append(str(v))
            n=n//2
            res=''.join(result)
        return int(res,2)
                
                

                
        