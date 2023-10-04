from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        par = []
        impar = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                par.append(nums[i])
            else:
                impar.append(nums[i])
        x = par.copy() + impar.copy()
        return(x)

objeto = Solution()
nums = [3, 1, 2, 4]
print(objeto.sortArrayByParity(nums))