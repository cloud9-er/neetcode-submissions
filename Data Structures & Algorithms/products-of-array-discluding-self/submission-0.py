import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            left=nums[0:i]
            right=nums[i+1:]
            l=math.prod(left)
            r=math.prod(right)
            sm=l*r
            res.append(sm)
        return res
        
        