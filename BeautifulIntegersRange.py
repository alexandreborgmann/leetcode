class Solution:
    def numberOfBeautifulIntegers(self, low, high, k):
        bonito=0

        for i in range(low,high+1):
            s=str(i)
            if i%k==0:
                somapar=0
                somaimpar=0
                for j in range(len(s)):
                    if int(s[j])%2==0:
                        somapar=somapar+1
                    else:
                        somaimpar=somaimpar+1
                #print(somapar,somaimpar,'j',j,'i=',i,'s=',s)
                if somapar==somaimpar:
                    bonito=bonito+1
        return(bonito)

objeto = Solution()

low = 10
high = 20
k = 3
print(objeto.numberOfBeautifulIntegers(low, high, k))

low = 1
high = 10
k = 1
print(objeto.numberOfBeautifulIntegers(low, high, k))
low = 5
high = 5
k = 2
print(objeto.numberOfBeautifulIntegers(low, high, k))