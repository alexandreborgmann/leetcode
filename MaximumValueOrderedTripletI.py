from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maior=0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[i]>nums[j]:
                    for k in range(j+1,len(nums)):
                        valor = (nums[i] - nums[j]) * nums[k]
                        if maior<valor:
                            maior = valor
                            #print(i,j,k,maior,nums[i],nums[j],nums[k])
        return(maior)

objeto = Solution()
nums = [12, 6, 1, 2, 7]
nums = [6,14,20,19,19,10,3,15,12,13,8,1,2,15,3]
#nums = [1000000,1,1000000]
print(objeto.maximumTripletValue(nums))