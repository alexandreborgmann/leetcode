from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            val = nums[i+1]
            for j in range(freq):
                output.append(val)
        return(output)

objeto = Solution()
#nums = [1,2,3,4]
nums = [1,1,2,3]
print(objeto.decompressRLElist(nums))
