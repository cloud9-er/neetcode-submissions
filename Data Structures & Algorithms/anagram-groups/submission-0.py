class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        boxes={}
        for words in strs:
            sort=''.join(sorted(words))
            if sort not in boxes:
                boxes[sort]=[]
            boxes[sort].append(words)
        return list((boxes).values())
        

                            