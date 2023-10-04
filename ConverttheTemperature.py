class Solution(object):
    def convertTemperature(self, celsius):
        lista = []
        kelvin = round(celsius + 273.15,5)
        fahrenheit = round(celsius * 1.80 + 32.00,5)
        lista.append(kelvin)
        lista.append(fahrenheit)
        return lista

celsius = 36.50

objeto = Solution()
print(objeto. convertTemperature(celsius))