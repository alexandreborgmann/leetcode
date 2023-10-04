class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        simetricos = 0
        for i in range(low,high+1):
            stri = str(i)
            if len(stri)%2==0:
                tamanho=int(len(stri)/2)
                listai=list(stri)
                somaInicio=0
                somaFim=0
                for j in range(tamanho):
                    somaInicio=somaInicio+int(listai[j])
                    somaFim=somaFim+int(listai[j+tamanho])
                    #print(tamanho,j,somaInicio,somaFim, listai[j],listai[j+tamanho])
                if somaInicio == somaFim:
                    #print(somaInicio,somaFim,listai)
                    simetricos = simetricos + 1
        return(simetricos)

objeto = Solution()
low = 1
high = 100
#low = 1200
#high = 1230
print(objeto.countSymmetricIntegers(low, high))