class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        soma=0
        produto=1
        for i in range(len(s)):
            soma = soma + int(s[i])
            produto = produto * int(s[i])
        return produto-soma

n = 4421
objeto = Solution()
print(objeto. subtractProductAndSum(n))