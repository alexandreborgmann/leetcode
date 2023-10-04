class Solution(object):
    def numIdenticalPairs(self, nums):
        iguais=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    iguais+=1
                print('i=',i,'j=',j,'nums[i]=',nums[i],'nums[j]=',nums[j])
        return iguais

objeto = Solution()
#nums = [1,2,3,1,1,3]
#nums = [1,1,1,1]
nums = [1,2,3]
print(objeto.numIdenticalPairs(nums))