class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2=[] # in here we are creating a list that will contail the duplicates of the first array 
        for num in nums:# this is a loop that will collect all the values in the nums array 
            nums2.append(num)# this will add all the values we looped through into the new array we initialized,num2
        ans=nums + nums2 #this will concatenate the two arrays into one array called the ans array 
        return ans


        