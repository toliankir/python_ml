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

    def clacMixMaxOnRange(self, start, end, delta):
        min = max = self.calcFunc(start)
        while start <= end:
            start += delta
            result = self.calcFunc(start)
            if result < min:
                min = result
            if result > max:
                max = result
        return min, max


f1 = MathFunction(3.1, 10.3, -2.8, 10.3)
f2 = MathFunction(2.1, 8.8, -11.4, -5.6)
f3 = MathFunction(1.6, 0.2, -20.8, 38.5)

min, max = f1.clacMixMaxOnRange(-4, 1, 0.0001)
print("min:{:.4f} max:{:.4f}".format(min,max))

min, max = f2.clacMixMaxOnRange(-4, 1, 0.0001)
print("min:{:.4f} max:{:.4f}".format(min,max))

min, max = f3.clacMixMaxOnRange(-4, 1, 0.0001)
print("min:{:.4f} max:{:.4f}".format(min,max))
