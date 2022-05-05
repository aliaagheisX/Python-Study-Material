class Point :
    x = 0
    y = 0
    def Read(self) :
        self.x = int(input("Enter X : "))
        self.y = int(input("Enter Y : "))
    def Print(self) : 
        print(f"X: {self.x} | Y: {self.y}")
    def get_dist(p1, p2):
        return ((p1.X - p2.X) ** 2 + (p1.Y - p2.Y) ** 2) * 0.5

class Line :
    Point1 = Point()
    Point2 = Point()
    def Read(self):
        self.Point1.Read()
        self.Point2.Read()

    def Print(self):
        self.Point1.Print()
        self.Point2.Print()
    
    def Get_Length(self):
        return self.Point1.get_dist(self.Point2)

    def is_vertical(self):
        return (self.Point1.x - self.Point2.x) == 0 

    def Get_Slop(self):
        if self.is_vertical() : return "undefined"
        return (self.Point1.y - self.Point2.y) / (self.Point1.x - self.Point2.x)

l1 = Line()

l1.Read()

print(l1.Get_Slop())
