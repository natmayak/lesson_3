class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def coordinates(self):
        print(f'Coordinates are: a {self.a}, b {self.b}')

    def __repr__(self):
        return f'<Point a: {self.a}, b: {self.b}>'

my_point = Point(1, 3)
my_point.coordinates()
print(my_point)

