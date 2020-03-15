def midpoint1(x1: float, y1: float) -> complex:
    """ Returns the Midpoint of a line, assuming one points is 0,0"""

    x = x1 / 2
    y = y1 / 2

    return complex(x, y)


def midpoint2(x1: float, y1: float, x2: float, y2: float) -> complex:
    """ Returns the Midpoint between two numbers on a line"""

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    return complex(x, y)


def expI(exponent: float) -> complex:
    """Returns what I to an exponent equals"""

    trueExponent = exponent % 4
    if(trueExponent == 0):
        return 1
    elif(trueExponent == 1):
        return complex(0, 1)
    elif(trueExponent == 2):
        return -1
    elif(trueExponent == 3):
        return complex(0, -1)


def distance(x1: float, y1: float, x2: float, y2: float) -> complex:
    """Returns an unsquared distance between to points"""
    return ((x2 - x1) ** 2) + ((y2 - y1) ** 2)


def distance2(x1: float, y1: float, x2: float, y2: float) -> float:
    """Returns the distance between to points"""
    return math.hypot(x2 - x1, y2 - y1)


def complexDivide(numerator: float, denominator: float) -> (float, float):
    """Returns a rational number of dividing two complex numbers"""
    DenomConjugate = denominator.conjugate()
    denominator *= DenomConjugate
    numerator *= DenomConjugate

    return numerator, denominator


