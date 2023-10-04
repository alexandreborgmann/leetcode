from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        novo = []
        soma =0
        indice =0
        for i in range(len(nums)):
            soma +=nums[i]
            indice +=1
            if soma==target:
                break
            if soma>target:
                soma = 0
                indice = 0
            print(i,soma,indice)
        return(indice)

objeto = Solution()
nums = [1,2,3]
target = 5
print(objeto.minSizeSubarray(nums, target))