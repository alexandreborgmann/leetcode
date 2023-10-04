class Solution(object):
    def longestCommonPrefix(self, strs):
        menorString=len(strs[0])
        for i in range(len(strs)):
            if len(strs[i])<menorString:
                menorString=len(strs[i])
        s=''
        for j in range(menorString):
            caracter=strs[0][j]
            for i in range(len(strs)):
                if caracter!=strs[i][j]:
                    return(s)
            s=s+caracter
        return s

objeto = Solution()

#strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]

print(objeto.longestCommonPrefix(strs))
