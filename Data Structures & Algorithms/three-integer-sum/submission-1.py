class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st=sorted(nums)
        res=[]
        for i in range(len(st)-2):
            if i>0 and st[i]==st[i-1]:
                continue
            left=i+1
            right=len(st)-1
            while left<right:
                total=st[i]+st[left]+st[right]
                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    res.append([st[i],st[left],st[right]])
                    left+=1
                    right-=1
                    while left<right and st[left]==st[left-1]:
                        left+=1
                    while left<right and st[right]==st[right+1]:
                        right-=1
        return res     