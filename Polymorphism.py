class lamborgini():
    def Maxspeed(self):
        print("the max speed is 221mph")
    def founded(self):
        print("it was founded in 1963")
    def founder(self):
        print("Ferrucio Lamborgini founded lamborgini")
class ferrari():
    def Maxspeed(self):
        print("the max speed is 200mph")
    def founded(self):
        print("founded in 1988")
    def founder(self):
        print(self)
        print("founded by Enzo Ferrari")

obj_ind=lamborgini()
obj_usa=ferrari()
for country in(obj_ind,obj_usa):
    country.Maxspeed()
    country.founded()
    country.founder()
    