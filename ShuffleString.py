from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r = ['']*len(s)
        for i in range(len(s)):
            r[indices[i]] = s[i]
        s1 = ''.join(r)
        return(s1)

objeto = Solution()
#s = "codeleet"
#indices = [4,5,6,7,0,2,1,3]
s = "abc"
indices = [0,1,2]
print(objeto.restoreString(s, indices))