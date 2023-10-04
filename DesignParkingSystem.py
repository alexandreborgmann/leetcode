class ParkingSystem(object):
    def __init__(self, big, medium, small):
        self.park=[big, medium, small]

    def addCar(self, carType):
        if self.park[carType-1]==0:
            return False
        else:
            self.park[carType-1]-=1
            return True

#obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)