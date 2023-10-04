class Solution:
    def maxSum(self, nums):
        resposta=0
        for i in range(len(nums)-1):
            numero=nums[i]+nums[i+1]

            if nums[i]>9:
                numstraux=str(nums[i])
                numerostr1=str(int(numstraux[0])+int(numstraux[1]))
            else:
                numerostr1=str(nums[i])

            if nums[i+1]>9:
                numstraux=str(nums[i+1])
                numerostr2=str(int(numstraux[0])+int(numstraux[1]))
            else:
                numerostr2=str(nums[i+1])

            numerostr=numerostr1+numerostr2
            print(nums[i], nums[i + 1], 'numero=',numero, numerostr1, numerostr2, numerostr, resposta)
            
            if numero == int(numerostr) :
                if numero > resposta:
                    resposta=numero
        if resposta==0:
            resposta=-1
        return(resposta)

objeto = Solution()
#nums = [51, 71, 17, 24, 42]
#nums =[1,2,3,4]
nums = [31,25,72,79,74]
print(objeto.maxSum(nums))

'''
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            for j in range(i):
                if max(str(nums[i])) == max(str(nums[j])):
                    ans = max(ans, nums[i] + nums[j])
        return ans
'''