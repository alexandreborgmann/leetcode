class Solution(object):
    def getConcatenation(self, nums):
        numfinal = []
        tamanho = len(nums)
        for i in range(tamanho):
            numfinal.insert(i,nums[i])
            numfinal.insert(i+tamanho,nums[i])
        return numfinal

objeto = Solution()
nums = [1, 2, 1]
print(objeto.getConcatenation(nums))