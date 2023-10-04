from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ascendente = 'true'
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                ascendente = 'false'
                break
        descendente = 'true'
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                descendente = 'false'
                break
        if ascendente == 'true' or descendente == 'true':
            return(True)
        else:
            return(False)

objeto = Solution()
#nums = [1,2,2,3]
#nums = [6,5,4,4]
nums = [1,3,2]
print(objeto.isMonotonic(nums))