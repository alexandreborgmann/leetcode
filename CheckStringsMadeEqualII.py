import sortedcontainers
from typing import List

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return(True)
        for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                s1novo = list(s1)
                if (j-i)%2==0:
                    auxiliar=s1novo[i]
                    s1novo[i]=s1novo[j]
                    s1novo[j]=auxiliar
                    if s1novo==list(s2):
                        return(True)
                    #print('1i',i,'s1novo',s1novo,'lists2',list(s2))
        for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                s2novo=list(s2)
                if (j-i)%2==0:
                    auxiliar=s2novo[i]
                    s2novo[i]=s2novo[j]
                    s2novo[j]=auxiliar
                    if s2novo==list(s1):
                        return (True)
                #print('2',i,s2novo,list(s1))
        s1novo = list(s1)
        for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                if (j-i)%2==0 and i<j:
                    auxiliar=s1novo[i]
                    s1novo[i]=s1novo[j]
                    s1novo[j]=auxiliar
                    if s1novo==list(s2):
                        return(True)
                    print('3','i',i,'j',j,'s1novo',s1novo,'lists2',list(s2),'(j-i)',(j-i))
        s2novo = list(s2)
        for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                if (j-i)%2==0:
                    auxiliar=s2novo[i]
                    s2novo[i]=s2novo[j]
                    s2novo[j]=auxiliar
                    #print('4',i,'s2novo',s2novo,'list s1',list(s1),'auxiliar',auxiliar,s1novo[i+2])
                    if s2novo==list(s1):
                        return (True)
        #print('final',s1novo,list(s1))
        return(False)

objeto = Solution()
s1 = "abcdba"
s2 = "cabdab"
print(objeto.canBeEqual(s1, s2))