class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        conta = 0
        for i in range(len(hours)):
            if hours[i]>=target:
                conta = conta + 1
        return(conta)

objeto = Solution()
#hours = [0,1,2,3,4]
#target = 2
hours = [5,1,4,2,2]
target = 6
print(objeto.numberOfEmployeesWhoMetTarget(hours, target))