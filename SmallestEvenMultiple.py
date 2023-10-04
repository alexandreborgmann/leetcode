class Solution(object):
    def smallestEvenMultiple(self, n):
        for i in range(1,10000):
            if i%n==0 and i%2==0:
                return(i)
        return(-1)

objeto = Solution()
n = 77
if n < 1 or n >150:
    exit(1)
print(objeto.smallestEvenMultiple(n))
