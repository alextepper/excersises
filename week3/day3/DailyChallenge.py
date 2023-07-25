import math

class Cirlce:
    def __init__(self, radius=None, diameter=None):
        if radius is not None and diameter is not None:
            raise ValueError("Both radius and diameter cannot be specified at the same time.")

        if radius is not None:
            self.radius = radius
            self.diameter = 2 * radius
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be specified.")

    def get_area(self):
        return self.radius*math.pi**2

    def __str__(self):
        return f"The circle's radius is {self.radius}, and it's diameter is {self.diameter}"

    def __add__(self, other):
        return self.get_area() + other.get_area()

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __repr__(self):
        return str(self.radius) + "-" + str(self.diameter) + "-" + str(self.get_area())


circle1 = Cirlce(radius=10)
circle2 = Cirlce(radius=14)
circle3 = Cirlce(radius=4)
circle4 = Cirlce(radius=65)

list = [circle1, circle2, circle4, circle3]

print(list)

list.sort()

print(list)