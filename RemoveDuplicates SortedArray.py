class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tamanho=len(nums)
        i=0
        while i<tamanho-1:
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
                tamanho=tamanho-1
            else:
               i=i+1
        return len(nums)

objeto = Solution()

nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
objeto.removeDuplicates(nums)
#print(nums)