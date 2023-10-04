import sortedcontainers
from typing import List

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        srt = sortedcontainers.SortedList()
        mn = abs(nums[-1] - nums[0])
        for j, num in enumerate(nums):
            if j >= x:
                srt.add(nums[j - x])
            it = srt.bisect_left(num)
            if it < len(srt):
                mn = min(mn, abs(srt[it] - num))
            if it > 0:
                mn = min(mn, abs(srt[it - 1] - num))
        return mn

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

