class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisthis(self):
        print(Bird)
    def swim(self):
        print("Swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is Ready")
    def whoisthis(self):
            print("Penguin")
    def run(self):
            print("run faster")

peggy=Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()
            