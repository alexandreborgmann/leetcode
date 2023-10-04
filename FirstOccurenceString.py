class Solution(object):
    def strStr(self, haystack, needle):
        tamanhoi = len(haystack) - 1
        tamanhoj = len(needle) - 1
        i = 0
        j = 0
        achouPrimeiro = -1
        if tamanhoj>tamanhoi:
            return(-1)
        while i<=tamanhoi:
            print('i=',i,'j=',j,haystack[i],needle[j],'achouPrimeiro=',achouPrimeiro)
            if haystack[i] != needle[j]:
               if achouPrimeiro!=-1:
                    i=j-1
               achouPrimeiro=-1
               j = 0
            else:
                if achouPrimeiro==-1:
                    achouPrimeiro = i
                j = j + 1
                if j > tamanhoj:
                    return achouPrimeiro
            i = i + 1
        return(achouPrimeiro)

objeto = Solution()
haystack = "sadbutsad"
needle = "sad"
#haystack = "leetcode"
#needle = "leeto"
#haystack = "aaa"
#needle = "aaaa"
#haystack = "mississippi"
#needle = "issip"
haystack = "mississippi"
needle = "issipi"
print(objeto.strStr(haystack, needle))