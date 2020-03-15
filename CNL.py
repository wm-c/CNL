import math
import cmath



# Returns the Midpoint of a line, assuming one points is 0,0
def midpoint1(x1,y1):
    x = x1 / 2
    y = y1 / 2

    return complex(x, y)

# Returns the Midpoint between two numbers on a line
def midpoint2(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    return complex(x, y)

# Returns what I to an exponent equals
def expI(exponent):
    trueExponent = exponent % 4
    if(trueExponent == 0):
        return 1
    elif(trueExponent == 1):
        return complex(0,1)
    elif(trueExponent == 2):
        return -1
    elif(trueExponent == 3):
        return complex(0,-1)


# Returns an unsquared distance between to points
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2) + ((y2 - y1) ** 2)

# Returns the distance between to points
def distance2(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

# Returns a rational number of dividing two complex numbers
def complexDivide(numerator, denominator):
    DenomConjugate = denominator.conjugate()
    denominator *= DenomConjugate
    numerator *= DenomConjugate

    return numerator, denominator

print(complexDivide(complex(-6, 8), complex(-4, -3)))


