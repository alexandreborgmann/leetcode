class Solution(object):
    def decodeMessage(self, key, message):
        alfabetoa = { 'a': 1, 'b':2, 'c':3, 'd':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26 }
        alfabeton = { 1:'a', 2:'b', 3:'c', 4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z' }
        chaveUnica = {}
        j = 1
        for i in range(len(key)):
            if key[i]!=' ':
                incluir = 1
                for x in chaveUnica.keys():
                    if x == key[i]:
                        incluir = 0
                        break
                if incluir == 1:
                    chaveUnica[key[i]] = j
                    j = j + 1
        resposta=""
        for i in range(len(message)):
            if message[i] == ' ':
                resposta=resposta+message[i]
            else:
                resposta=resposta+alfabeton[chaveUnica[message[i]]]
        return(resposta)

objeto = Solution()
#key = "eljuxhpwnyrdgtqkviszcfmabo"
#message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(objeto.decodeMessage(key, message))