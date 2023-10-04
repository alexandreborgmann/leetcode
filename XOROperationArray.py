class Solution(object):
    def xorOperation(self, n, start):
        lista = []
        for i in range(0,n):
            lista.append(start + 2 * i)

            if i>0:
                if i==1:
                    somaXor = lista[i-1] ^ lista[i]
                else:
                    somaXor = somaXor ^ lista[i]
        if n==1:
            somaXor=start
        return(somaXor)

objeto = Solution()
n = 1
start = 7
print(objeto.xorOperation(n, start))