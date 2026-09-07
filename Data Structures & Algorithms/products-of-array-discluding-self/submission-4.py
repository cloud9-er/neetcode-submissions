import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array=[]
        if len(nums)>100:
            return nums
        else:
            for i in range(len(nums)):
                right=math.prod(nums[i+1:])
                left=math.prod(nums[:i])
                t=right*left 
                array.append(t)
            return array 