from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        primeiro = []
        segundo = []
        for i in range(len(nums)):
            if i<n:
                primeiro.append(nums[i])
            else:
                segundo.append(nums[i])
        resultado = []
        for i in range(n):
            resultado.append(primeiro[i])
            resultado.append(segundo[i])
        return(resultado)

objeto = Solution()
'''
nums = [2,5,1,3,4,7]
n = 3
nums = [1,2,3,4,4,3,2,1]
n = 4
'''
nums = [1,1,2,2]
n = 2
print(objeto.shuffle(nums, n))