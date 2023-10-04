from typing import List

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        lista = list(s)
        qtdUm = lista.count('1')
        if qtdUm==1:
            s='0'*(len(s)-1)+'1'
        if qtdUm>=2:
            s='1'*(qtdUm-1)+'0'*(len(s)-qtdUm)+'1'
        #print('s=',s,qtdUm)
        return(s)

objeto = Solution()
s = "010"
#s = "1010"
print(objeto.maximumOddBinaryNumber(s))