from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            for j in range(i + 1, n):
                if max(str(nums[i])) == max(str(nums[j])):
                    ans = max(ans, nums[i] + nums[j])
                print(str(nums[i]),max(str(nums[i])),str(nums[j]),max(str(nums[j])),ans)

        return ans

objeto = Solution()
#nums = [51, 71, 17, 24, 42]
#nums =[1,2,3,4]
nums = [31,25,72,79,74]
print(objeto.maxSum(nums))