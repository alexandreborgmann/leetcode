class Solution(object):
    def mostWordsFound(self, sentences):
        maiorPalavra = 0
        for i in range(len(sentences)):
            palavras = 1
            achouCaracter = 0
            for j in range(len(sentences[i])):
                if sentences[i][j] == ' ':
                    if achouCaracter == 1:
                        palavras = palavras + 1
                        achouCaracter = 0
                else:
                    achouCaracter = 1

            if maiorPalavra<palavras:
                maiorPalavra = palavras
        return(maiorPalavra)

objeto = Solution()
#sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
sentences = ["please wait", "continue to fight", "continue to win"]
print(objeto.mostWordsFound(sentences))