class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        soma = 0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if jewels[j]==stones[i]:
                    soma = soma +1
        return(soma)

objeto = Solution()
#jewels = "aA"
#stones = "aAAbbbb"
jewels = "z"
stones = "ZZ"
print(objeto.numJewelsInStones(jewels, stones))