from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maior=-1
        pre = [0]*len(nums)
        suf = [0]*len(nums)
        for i in range(1, len(nums)):
            pre[i]=max(pre[i-1], nums[i-1])
        for i in range(len(nums)-2,0,-1):
            suf[i] = max(suf[i+1],nums[i+1])
        for i in range(len(nums)):
            x = (pre[i] - nums[i]) * suf[i]
            maior = max(maior, x)
        return(maior)

objeto = Solution()
#nums = [12, 6, 1, 2, 7]
#nums = [1,10,3,4,19]
nums = [1,2,3]
#nums = [1000000,1,1000000]
#nums = [18,15,8,13,10,9,17,10,2,16,17]
#nums =[5,7,8,4]
print(objeto.maximumTripletValue(nums))


'''
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maior=0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[i]>nums[j]:
                    nroMax = max(nums[j+1:])
                    valor = (nums[i] - nums[j]) * nroMax
                    if maior<valor:
                        maior = valor
                        print(i,j,maior,nums[i],nums[j],nroMax)
        return(maior)

objeto = Solution()
nums = [12, 6, 1, 2, 7]
nums = [6,14,20,19,19,10,3,15,12,13,8,1,2,15,3]
#nums = [1000000,1,1000000]
print(objeto.maximumTripletValue(nums))


'''