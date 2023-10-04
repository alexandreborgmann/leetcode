class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if target==nums[i]:
                return i
            if nums[i]>target:
                return i
        return(len(nums))
'''
nums = [1,3,5,6]
target = 5
nums = [1,3,5,6]
target = 2
'''
nums = [1,3,5,6]
target = 7
objeto = Solution()
print(objeto.searchInsert(nums,target))