class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s)==1:
            return False

        listaAbre=['(', '{', '[']
        listaFecha=[')', '}', ']']

        listaEntrada=[]

        Retorna=False
        for i in range(len(s)):
            if i==0 and listaAbre.__contains__(s[i])==False:
                return False
            if listaAbre.__contains__(s[i]) == True:
                listaEntrada.append(s[i])
            else:
                if listaFecha.__contains__(s[i]) == True:
                    if len(listaEntrada)==0:
                        return False
                    if listaAbre.index(listaEntrada.pop()) != listaFecha.index(s[i]):
                        return False
                    Retorna = True
        if len(listaEntrada)!=0:
            return False
        return Retorna
'''
Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''
s = "([]){"
if len(s)<0 or len(s)>=(10**4):
    exit(1)

objeto = Solution()

print(objeto.isValid(s))
