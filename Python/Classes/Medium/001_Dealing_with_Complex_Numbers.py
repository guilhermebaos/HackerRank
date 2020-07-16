import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary

    def __add__(self, no):
        r = self.real + no.real
        i = self.imag + no.imag
        return Complex(r, i)

    def __sub__(self, no):
        r = self.real - no.real
        i = self.imag - no.imag
        return Complex(r, i)

    def __mul__(self, no):
        r = self.real * no.real - self.imag * no.imag
        i = self.real * no.imag + self.imag * no.real
        return Complex(r, i)

    def __truediv__(self, no):
        r = (self.real * no.real + self.imag * no.imag) / (no.real ** 2 + no.imag ** 2)
        i = (self.imag * no.real - self.real * no.imag) / (no.real ** 2 + no.imag ** 2)
        return Complex(r, i)

    def mod(self):
        r = (self.real ** 2 + self.imag ** 2) ** 0.5
        i = 0
        return Complex(r, i)

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result
