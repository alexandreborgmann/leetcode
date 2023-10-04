class Solution(object):
    def addTwoNumbers(self, l1, l2):
        numero1 = 0
        tamanho = len(l1) - 1
        i = tamanho
        while i >= 0:
            numero1 = numero1 + l1[i] * 10 ** (tamanho - i)
            i = i - 1
        numero2=0
        tamanho = len(l2) - 1
        i = tamanho
        while i >= 0:
            numero2 = numero2 + l2[i] * 10 ** (tamanho - i)
            i = i - 1
        l3 = []
        strNumero = str(numero1 + numero2)
        for i in range(len(strNumero)-1,-1,-1):
            l3.append(int(strNumero[i]))
        #print(l1,l2)
        return(l3)

objeto = Solution()
'''
l1 = [2,4,3]
l2 = [5,6,4]
l1 = [0]
l2 = [0]
'''
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(objeto.addTwoNumbers(l1,l2))