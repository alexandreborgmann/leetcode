class Solution:
    def minimumOperations(self, num: str) -> int:
        delecoes = 0
        numi=num
        if int(numi) % 25 == 0:
            return delecoes
        while len(numi)>=2:
            numi = numi[1:]
            delecoes = delecoes + 1
            if int(numi) % 25 == 0:
                print(1,numi, delecoes)
                return delecoes
        delecoes = 0
        numi = num
        while len(numi)>=2:
            numi = numi[0:len(numi)-1]
            delecoes = delecoes + 1
            if int(numi) % 25 == 0:
                print(2,numi, delecoes)
                return delecoes
        
        return(None)
objeto = Solution()
#num = "2245047"
num = "2908305"
#num = "10"
print(objeto.minimumOperations(num))