class Solution(object):
    def romanToInt(self, numeroRomano):
        valoresRomanos = { 'I': 1, 'V' :5, 'X': 10, 'L' : 50, 'C' :100, 'D': 500, 'M': 1000}

        tamanho = len(numeroRomano)
        i = 0
        numeroDecimal=0
        while i < tamanho:
            if i==tamanho - 1:
                numeroDecimal = numeroDecimal + int(valoresRomanos.get(numeroRomano[i]))
            else:
                if numeroRomano[i] == 'I' and numeroRomano[i + 1]=='V':
                    numeroDecimal= numeroDecimal + 4
                    i = i + 1
                elif numeroRomano[i] == 'I' and numeroRomano[i + 1]=='X':
                    numeroDecimal = numeroDecimal + 9
                    i = i + 1
                elif numeroRomano[i] == 'X' and numeroRomano[i + 1] == 'L':
                    numeroDecimal = numeroDecimal + 40
                    i = i + 1
                elif numeroRomano[i] == 'X' and numeroRomano[i + 1] == 'C':
                    numeroDecimal = numeroDecimal + 90
                    i = i + 1
                elif numeroRomano[i] == 'C' and numeroRomano[i + 1] == 'D':
                    numeroDecimal = numeroDecimal + 400
                    i = i + 1
                elif numeroRomano[i] == 'C' and numeroRomano[i + 1] == 'M':
                    numeroDecimal = numeroDecimal + 900
                    i = i + 1
                else:
                    numeroDecimal = numeroDecimal + int(valoresRomanos.get(numeroRomano[i]))
            i = i + 1
        return numeroDecimal

objeto = Solution()

#numeroRomano="III"
#numeroRomano="LVIII"
numeroRomano="MCMXCIV"

print(objeto.romanToInt(numeroRomano))
