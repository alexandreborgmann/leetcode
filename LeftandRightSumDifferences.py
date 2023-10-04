from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        soma = 0
        esquerda = []
        for i in range(len(nums)):
#            print(i,soma)
            esquerda.append(soma)
            soma += nums[i]

        soma = 0
        direita = nums.copy()
        for i in range(len(nums)-1,-1,-1):
#            print(i,soma)
            direita[i]=soma
            soma += nums[i]
#        print(esquerda)
#        print(direita)
        resposta = []
        for i in range(len(esquerda)):
            resposta.append(abs(esquerda[i]-direita[i]))
        return(resposta)

objeto = Solution()
nums = [10,4,8,3]
nums = [1]
print(objeto.leftRightDifference(nums))