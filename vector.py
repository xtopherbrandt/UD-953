import math

class Vector(object):

                
    @staticmethod
    def Zero(dimensions):
        return Vector( [0] * dimensions )

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        return Vector( map( lambda x, y: x + y, self.coordinates, other.coordinates ) )

    def __sub__(self, other):
        return Vector( map( lambda x, y: x - y, self.coordinates, other.coordinates ) )

    def __mul__(self, other):
        if type(other) is float or type(other) is int: 
            return Vector( map( lambda x: x * other, self.coordinates) )
        elif type(other) is Vector:
            return reduce( lambda x, y: x + y, map( lambda x, y: (x * y), self.coordinates, other.coordinates ))

    def __abs__(self):
        return Vector( map( lambda x: abs(x), self.coordinates ))

    def round(self, num_digits = 0):
        return Vector( map( lambda x: round(x, num_digits), self.coordinates ))

    def magnitude(self):
        return math.sqrt( reduce( lambda x,y: x + y, map( lambda x: math.pow(x,2), self.coordinates )))

    def direction(self):
        return self * ( 1 / self.magnitude() )

    def unit(self):
        return self.direction()

    def angle(self, other, radians=True):
        if radians:
            return math.acos( (self * other) / (self.magnitude() * other.magnitude()))
        else:
            return math.degrees( math.acos( (self * other) / (self.magnitude() * other.magnitude())))

    def isOrthogonal(self, other):
        return True if round(( self * other ), 10) == 0 else False

    def isZero(self):
        return True if round(self.magnitude(),10) == 0 else False

    def isParallel(self, other):
        return (self.isZero() or other.isZero() or self.angle( other ) == 0 or self.angle( other ) == math.pi )

    '''
    Projection of a vector, other, on to this vector
    '''
    def proj(self, other):
        return self.unit() * (self.unit() * other)

    '''
    Opposite of projection, this function finds the projection of this vector parallel (on to) the other
    '''
    def parallelTo(self, basis):
        return basis.unit() * (basis.unit() * self)

    '''
    The vector perpendicular to the basis vector that adds to the parallel vector to equal this vector
    '''
    def perpendicularTo(self, basis):
        return self - self.parallelTo( basis )
    
    '''
    Computes the cross product of 2 3-dimensional vectors
    '''
    def cross(self, other):
        if len(self.coordinates) != 3 :
            print "Can only cross 3D vectors"
            return Vector.Zero()
        x1 = self.coordinates[0]
        y1 = self.coordinates[1]
        z1 = self.coordinates[2]
        x2 = other.coordinates[0]
        y2 = other.coordinates[1]
        z2 = other.coordinates[2]
        return Vector([(y1 * z2)-(y2*z1), -1 * ((x1 * z2)-(x2 * z1)), (x1 * y2)-(x2 * y1)])
    
    def areaSpannedTo(self, other):
        return self.cross(other).magnitude()

    def areaOfTriangleTo(self, other):
        return self.areaSpannedTo(other) * 0.5