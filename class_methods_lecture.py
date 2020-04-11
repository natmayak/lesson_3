class Point:
    a = 0
    b = 0.7
# my_point = Point()
# print(my_point.a)
# my_point.a = 10
# print(my_point.a)

    def coordinates(self):
        print(f'coordinates are: {self.a}, {self.b}')

my_point = Point()
print(my_point)
my_point.coordinates()
my_point.a = 10
my_point.coordinates()