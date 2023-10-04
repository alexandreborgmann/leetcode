class Solution(object):
    def minAbsoluteDifference(self, nums, x):
        minimo=-1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= x:
                    if minimo==-1:
                        minimo=abs(nums[i] - nums[j])
                    elif abs(nums[i] - nums[j])<minimo:
                        minimo=abs(nums[i] - nums[j])
                    #print(i,j,nums[i],nums[j],'minimo=',minimo)
        return(minimo)


objeto = Solution()

nums = [4,3,2,4]
x = 2
'''
nums = [5,3,2,10,15]
x = 1

nums = [1,2,3,4]
x = 3
'''
print(objeto.minAbsoluteDifference(nums, x))
