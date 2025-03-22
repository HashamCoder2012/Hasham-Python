class India():
    def capital(self):
        print("New Dehli ia the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language")
    def type(self):
        print("India is developing country")
class USA():
    def capital(self):
        print("Watshington ,DC is the capital")
    def language(self):
        print("English is the primary language")
    def type(self):
        print(self)
        print("Usa is already a developed country")

obj_ind=India()
obj_usa=USA()
for country in(obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()
    