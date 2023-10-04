import sortedcontainers
from typing import List

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return(True)
        for i in range(0,len(s1)-2):
            s1novo = list(s1)
            auxiliar=s1novo[i]
            s1novo[i]=s1novo[i+2]
            s1novo[i + 2]=auxiliar
            if s1novo==list(s2):
                return(True)
            #print('1i',i,'s1novo',s1novo,'lists2',list(s2))
        for i in range(0,len(s2)-2):
            s2novo=list(s2)
            auxiliar=s2novo[i]
            s2novo[i]=s2novo[i+2]
            s2novo[i + 2]=auxiliar
            if s2novo==list(s1):
                return (True)
            #print('2',i,s2novo,list(s1))
        s1novo = list(s1)
        for i in range(0,len(s1)-2):
            auxiliar=s1novo[i]
            s1novo[i]=s1novo[i+2]
            s1novo[i + 2]=auxiliar
            if s1novo==list(s2):
                return(True)
            #print('3i',i,'s1novo',s1novo,'lists2',list(s2))
        s2novo = list(s2)
        for i in range(0,len(s2)-2):
            auxiliar=s2novo[i]
            s2novo[i]=s2novo[i+2]
            s2novo[i + 2]=auxiliar
            #print('4',i,'s2novo',s2novo,'list s1',list(s1),'auxiliar',auxiliar,s1novo[i+2])
            if s2novo==list(s1):
                return (True)
        #print('final',s1novo,list(s1))
        return(False)

objeto = Solution()
s1="ifjz"
s2="jzfi"
#s1 = "abcd"
#s2 = "cdab"
#s1 = "abcd"
#s2 = "dacb"
#s1="bnxw"
#s2="bwxn"
#s1="kina"
#s2="kina"
print(objeto.canBeEqual(s1, s2))