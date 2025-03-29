class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self._radius = radius
        elif diameter is not None:
            self._radius = diameter / 2  
        else:
            raise ValueError("Either radius or diameter must be provided")

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    def area(self):
        return 3.14159 * (self._radius ** 2)

    def __repr__(self):
        return f"Circle(radius={self._radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius



circle1 = Circle(radius=5)
circle2 = Circle(radius=3)
circle3 = Circle(diameter=10)

print(circle1.diameter)  
new_circle = circle1 + circle2
print(new_circle)

print(circle1 == circle2) 
print(circle1 < circle2)
print(circle1.area())  

