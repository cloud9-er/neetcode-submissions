class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res=[]
        for i in range(1,len(nums)):
            if nums[i] in res:
                return nums[i]
            else:
                res.append(nums[i])
        return -1