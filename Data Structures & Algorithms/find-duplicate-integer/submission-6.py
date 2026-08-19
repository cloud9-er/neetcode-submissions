class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            if i in res:
                return i
            res.append(i)
        return -1