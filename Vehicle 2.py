class Vehicle:
    def __init__(self,basefare):
        self.basefare=basefare
class Bus(Vehicle):
    def __init__(self,basefare,kms):
        self.kms=kms
        super().__init__(basefare)
    def calfare():
        print("Total fare:",basefare*kms)
citybus:bus(10,5)
citybus.calfare()
