class Solution(object):
    def lengthOfLastWord(self, s):
        x=s.rstrip(' ')
        i=len(x)-1
        while i>=0:
            if x[i]==' ':
                break
            i=i-1
        i=i+1
        return(len(x[i:]))

objeto = Solution()

#s = "Hello World"
#s = "   fly me   to   the moon  "
s = "luffy is still joyboy"
if len(s)<1 or len(s)>=10**4:
    exit(1)
print(objeto.lengthOfLastWord(s))