import cmath

# A complex number in the form x + yj, were j is the imaginary unit
num = complex(input())

# The absolute part of the polar coordinates is sqrt(x^2 + y^2)
print(abs(num))

# The phase is the oriented angle that joins the point (x, y) to the origin (0, 0)
print(cmath.phase(num))
