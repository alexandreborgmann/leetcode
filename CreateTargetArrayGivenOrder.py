from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return(target)

objeto = Solution()
#nums = [0,1,2,3,4]
#index = [0,1,2,2,1]
nums = [1,2,3,4,0]
index = [0,1,2,3,0]
print(objeto.createTargetArray(nums, index))