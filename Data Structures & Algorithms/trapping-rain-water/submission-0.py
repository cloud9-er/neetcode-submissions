class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        count=0
        for i in range(n-1):
            if height[i+1]>height[i]:
                t=height[i+1]-height[i]
                count+=t
            else:
                pass 
        return count+1
        