class Solution(object):
    def mySqrt(self, x):
        retorno = int(x ** (1/2))
        return(retorno)
x = 4
#x = 8
objeto = Solution()
if x < 1 or x >= 2 ** 31:
    exit(1)
print(objeto.mySqrt(x))