class Solution(object):
    def defangIPaddr(self, address):
        numLista = list(address.split("."))
        strRetorno = ''
        for i in range(len(numLista)-1):
            strRetorno = strRetorno + numLista[i] + '[.]'
        if len(numLista)>=1:
            strRetorno = strRetorno + numLista[i+1]
        #print(numLista,i,len(numLista))
        return(strRetorno)

objeto = Solution()
address = "1.1.1.1"
#address = "255.100.50.0"
print(objeto.defangIPaddr(address))