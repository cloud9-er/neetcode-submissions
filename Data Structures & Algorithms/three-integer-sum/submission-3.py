class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            a=nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]   
                if threeSum >0:
                    r-=1
                elif threeSum <0:
                    l+=1
                else:
                    res.append([a,nums[r],nums[l]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res


            