class Solution(object):
    def buildArray(self, nums):
        numfinal = []
        for i in range(len(nums)):
            numfinal.append(nums[nums[i]])
        return numfinal

objeto = Solution()
nums = [5,0,1,2,3,4]
print(objeto.buildArray(nums))