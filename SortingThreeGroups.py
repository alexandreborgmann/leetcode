from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        w=[0,0,0]
        for v in nums:
            w=[
                w[0]+(v!=1),
                min(w[:2])+(v!=2),
                min(w)+(v!=3)
            ]
        return min(w)

objeto = Solution()
nums = [2,1,3,2,1]
print(objeto.minimumOperations(nums))