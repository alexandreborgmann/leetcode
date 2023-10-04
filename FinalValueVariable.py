class Solution(object):
    def finalValueAfterOperations(self, operations):
        valores = { '++X' : 1, 'X++' : 1, '--X': -1, 'X--' : -1 }
        vlrRetorno = 0
        for i in range(len(operations)):
            vlrRetorno = vlrRetorno + int( valores[operations[i]])
        return(vlrRetorno)

objeto = Solution()
operations = ["--X","X++","X++"]
print(objeto.finalValueAfterOperations(operations))