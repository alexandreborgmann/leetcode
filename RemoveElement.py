class Solution(object):
    def removeElement(self, nums, val):
        i=0
        while i<len(nums):
            if val==nums[i]:
                nums.pop(i)
            else:
                i=i+1
        return(len(nums))

objeto = Solution()

#nums = [3,2,2,3]
#val = 3

nums =[0,1,2,2,3,0,4,2]
val=2
print(objeto.removeElement(nums, val))
#print(nums)