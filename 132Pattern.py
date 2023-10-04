from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        unicos = set(nums)
        if len(unicos)<3:
            return(False)
        i = 0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        print(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[k] and nums[k] < nums[j]:
                        return(True)
        return(False)

objeto = Solution()
#nums = [1,2,3,4]
#nums = [3,1,4,2]
#nums = [-1,3,2,0]
#nums = [3,5,0,3,4]
nums = [1,2,3,3,3,4,5,3]
print(objeto.find132pattern(nums))