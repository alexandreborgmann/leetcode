class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        resultado = []
        for i in range(len(nums)):
            somaMenor = 0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    somaMenor = somaMenor +1
            resultado.append(somaMenor)
        return(resultado)

objeto = Solution()
nums = [8,1,2,2,3]
print(objeto.smallerNumbersThanCurrent(nums))