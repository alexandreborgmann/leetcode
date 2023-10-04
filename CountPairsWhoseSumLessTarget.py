import sortedcontainers
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        resultado=0
        for i in range(len(nums)-1):
            for j in (range(i+1,len(nums),1)):
                #print('i=', i, 'j=', j, 'nums[i]', nums[i], 'nums[j]', nums[j], 'nums[i] + nums[j]=', nums[i] + nums[j])
                if nums[i] + nums[j] < target:
                    #print('entrei i=', i, 'j=', j, 'nums[i] + nums[j]',nums[i] + nums[j])
                    resultado = resultado + 1
        return(resultado)


objeto = Solution()
#nums = [-1,1,2,3,1]
#target = 2
nums = [-6,2,5,-2,-7,-1,3]
target = -2
print(objeto.countPairs(nums, target))