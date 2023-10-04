class Solution(object):
    def interpret(self, command):
        x = command.replace("()", "o")
        x = x.replace("(al)","al")
        return(x)

objeto = Solution()
#command = "G()(al)"
#command = "G()()()()(al)"
command = "(al)G(al)()()G"
print(objeto.interpret(command))
