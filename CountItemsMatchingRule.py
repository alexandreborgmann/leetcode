from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey=='type':
            indice = 0
        elif ruleKey=='color':
            indice = 1
        elif ruleKey=='name':
            indice = 2
        conta = 0
        for i in range(len(items)):
            #print(i, items[i], ruleKey, ruleValue)
            if items[i][indice]==ruleValue:
                conta += 1
        return(conta)

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
objeto = Solution()
print(objeto.countMatches(items, ruleKey, ruleValue))