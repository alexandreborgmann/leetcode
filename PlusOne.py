class Solution(object):
    def plusOne(self, digits):
        numero = 0
        tamanho = len(digits)-1
        i = tamanho
        while i >= 0:
            numero = numero + digits[i]*10**(tamanho-i)
            i = i - 1
        numero = numero + 1
        digitsNovo = []
        strNumero = str(numero)
        for i in range(len(strNumero)):
            digitsNovo.append(int(strNumero[i]))
        return(digitsNovo)
'''
digits = [1, 2, 3]
digits = [4,3,2,1]
digits = [9]
'''
digits = [9, 9]
if len(digits)>100 or len(digits)<=0:
    exit(1)
objeto = Solution()
print(objeto.plusOne(digits))
