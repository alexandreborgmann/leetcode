from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = []
        arr.append(first)
        for i in encoded:
            #print('arr[-1]',arr[-1],'i=',i)
            arr.append(arr[-1] ^ i)
            #print(arr)
        return arr

objeto = Solution()
#encoded = [1,2,3]
#first = 1
encoded = [6,2,7,3]
first = 4
print(objeto.decode(encoded, first))