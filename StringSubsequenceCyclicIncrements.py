from typing import List

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        i, j = 0, 0
        while j < n and i < m:
            c = str2[j]
            #print(str1[i],str1[i],'str2[j]=',str2[j],'i=',i,'j=',j)
            while i < m:
                #print('dentro=',i,str1[i])
                if str1[i] == c or chr(ord('a') + (ord(str1[i]) - ord('a') + 1) % 26) == c:
                    i += 1
                    j += 1
                    break
                i += 1
        return j == n

objeto = Solution()

str1 = "abc"
str2 = "ad"

print(objeto.canMakeSubsequence(str1, str2))
