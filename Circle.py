class circle():
    def __init__(self,r):
        self.radius =r
        
    def circle_area(self):
        return self.radius
    
newCircle = circle(360)
print("Dimension of Circle - radius : %d " %(newCircle.radius))
print("Area of circle :",newCircle.Circle_area())
