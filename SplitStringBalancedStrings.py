class Solution:
    def balancedStringSplit(self, s: str) -> int:
        contaR = 0
        contaL = 0
        balanceado = 0
        for i in range(len(s)):
            if s[i]=='R':
                contaR +=1
            else:
                contaL +=1
            if contaL==contaR:
                balanceado +=1
        return(balanceado)


objeto = Solution()
s = "RLRRLLRLRL"
s = "RLRRRLLRLL"
s = "LLLLRRRR"
print(objeto.balancedStringSplit(s))