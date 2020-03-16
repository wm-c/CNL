import math

class vector:
    '''Class for storing and calculating vector information'''

    def __init__(self, direction, magnitude):
        '''direction in degrees, length of vector'''
        self.direction = direction
        self.magnitude = magnitude
        self.endX, self.endY = self._Position()

    def setDirection(self, direction):
        '''Sets the direction'''
        self.direction = direction

    def setMagnitude(self, magnitude):
        '''Sets the magnitude'''
        self.magnitude = magnitude
    
    def __str__(self) -> str:
        return (f"{self.direction}, {self.magnitude}")

    def __repr__(self):
        return (f"{self.direction}, {self.magnitude}")
    
    def getValues(self) -> tuple:
        '''Returns direction and magnitude'''
        return self.direction, self.magnitude
    
    def _Position(self) -> tuple:
        '''Finds the x and y of the vector'''
        x = self.magnitude * math.cos(math.radians(self.direction))
        y = self.magnitude * math.sin(math.radians(self.direction))
        return x, y
