class dog:
    species="dogs"
    def __init__(self,name,age):
        self.name=name
        self.age=age
sweet=dog("sweet",10012)
kelly=dog("kelly",19300)
print("kelly is a {}".format(kelly.species))
print("sweet is also a {}".format(sweet.species))
print("{} is {} years old".format(kelly.name,kelly.age))
print("{} is {}years old".format(sweet.name,sweet.age))


        
