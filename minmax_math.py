import math

class MathFunction:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calcFunc(self, x):
        result = (self.a * pow(x, 3)) + (self.b *
                                         pow(x, 2)) + (self.c * x) + self.d
        return result

    def getExtremums(self):
        a = 3 * self.a
        b = 2 * self.b
        c = self.c
        d = pow(b, 2) - (4 * a * c)
        if (d < 0):
            return Exception("Can not calculate")
        x1 = ((-1 * b) + math.sqrt(d)) / (2 * a)
        x2 = ((-1 * b) - math.sqrt(d)) / (2 * a)
        return x1, x2

    def clacMixMax(self, points: list):
        min = max = self.calcFunc(points[0])
        for point in points[1:]:
            result = self.calcFunc(point)
            if result < min:
                min = result
            if result > max:
                max = result
        return min, max

    def calcMinMaxOnRange(self, start, end):
        points = list({start, end})
        x1, x2 = self.getExtremums()
        if x1 > start and x1 < end:
            points.append(x1)
        if x2 > start and x2 < end:
            points.append(x2)
        return self.clacMixMax(points)

f1 = MathFunction(3.1, 10.3, -2.8, 10.3)
f2 = MathFunction(2.1, 8.8, -11.4, -5.6)
f3 = MathFunction(1.6, 0.2, -20.8, 38.5)

min, max = f1.calcMinMaxOnRange(-4, 1)
print("min:{:.4f} max:{:.4f}".format(min,max))

min, max = f2.calcMinMaxOnRange(-4, 1)
print("min:{:.4f} max:{:.4f}".format(min,max))

min, max = f3.calcMinMaxOnRange(-4, 1)
print("min:{:.4f} max:{:.4f}".format(min,max))
