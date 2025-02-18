from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        length = self.length()
        if length == 0:
            return Vector(0, 1)
        return Vector(self.x / length, self.y / length)

    def __repr__(self):
        return f'({self.x:.2f}, {self.y:.2f})'


movement_speed = 3
position = Vector(0, 0)
target = Vector(30, 70)

while True:
    diff = target - position
    dist = (target - position).length()
    if dist < movement_speed:
        break
    movement_vector = diff.normalized() * movement_speed
    position += movement_vector
    print(position)

position = target
print(position)
