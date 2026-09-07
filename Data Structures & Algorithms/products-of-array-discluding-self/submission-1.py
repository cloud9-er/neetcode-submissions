import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array=[]
        for i in range(len(nums)):
           left=math.prod(nums[i+1:])
           print(left)
           right=math.prod(nums[:i])
           print(right)
           t=right*left 
           array.append(t)
        return array 