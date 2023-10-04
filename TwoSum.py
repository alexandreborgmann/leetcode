class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tamanhoArray=len(nums)
        for i in range(tamanhoArray):
            for j in range(i+1,tamanhoArray):
                print(f'[{i}{j}]= {nums[i]},{nums[j]}={(nums[i]+nums[j])} tamanhoArray={tamanhoArray}')
                if (nums[i]+nums[j])==target:
                    return [i, j]


#nums = [2,7,11,15]
#target = 9

#nums = [3,2,4]
#target = 6

#nums = [3,3]
#target = 6

nums=[3,2,3]
target = 6

if len(nums)<=1 or target>=(10**9):
    exit(1)

objeto = Solution()

print(objeto.twoSum(nums, target))