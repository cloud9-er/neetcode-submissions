import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=math.prod(nums)
        array=[]
        for i,n in enumerate(nums):
            if n==0:
                left=math.prod(nums[:i])
                right=math.prod(nums[i+1:])
                t=left*right
            else:
                t=int(p/n)
            array.append(t)
        return array