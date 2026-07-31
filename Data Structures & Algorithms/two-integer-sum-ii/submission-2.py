class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ls=[]
        for i in range(len(numbers)):
            for j in range(i+1):
                if numbers[i]+numbers[j] ==target and i !=j:
                    return [j+1,i+1]

        