import unittest
from vector import Vector

class VectorTests(unittest.TestCase):

    def test_AddingPositiveFloats(self):
        V1 = Vector([1.1,2,3])
        V2 = Vector([2,3,4.4])
        self.assertEqual( V1 + V2, Vector([3.1,5,7.4]))

    def test_AddingPositiveAndNegativeFloats(self):
        V1 = Vector([1.1,2,3])
        V2 = Vector([2,-3,4.4])
        self.assertEqual( V1 + V2, Vector([3.1,-1,7.4]))

    def test_SubtractPositiveFloats(self):
        V1 = Vector([1.1,2,3])
        V2 = Vector([2,3,4.4])
        
        #note that this assertion will fail on different machines, 
        # should implement abs and round in vector and use assertAlmostEqual
        self.assertEqual( (V1 - V2).round(1), Vector([-0.9,-1,-1.4]))

    def test_MultiplyByPositiveScalar(self):
        V1 = Vector([1.1,2,3])
        self.assertEqual( (V1 * 2.2).round(2), Vector([2.42,4.4,6.60]))

    def test_DotProductOfVectors(self):
        V1 = Vector([1.1, 2.2, 3.3])
        V2 = Vector([4.4, 5.5, 6.6])
        self.assertEqual( V1 * V2, 38.72 )

    def test_MultiplyByNegativeScalar(self):
        V1 = Vector([1.1,2,3])
        self.assertEqual( (V1 * -2.2).round(2), Vector([-2.42,-4.4,-6.60]))

    def test_AbsoluteValueOfVectorWithNegativeValues(self):
        V1 = Vector([-1, 2, -3])
        self.assertEqual( abs(V1), Vector([1 , 2, 3]))

    def test_RoundVectorCoordinatesTo2Digits(self):
        V1 = Vector([ 1.123, 4.456, 8.789 ])
        self.assertEqual( V1.round(2), Vector( [1.12, 4.46, 8.79]))

    def test_RoundVectorCoordinatesTo0Digits(self):
        V1 = Vector([ 1.123, 4.456, 8.789 ])
        self.assertEqual( V1.round(), Vector( [1.0, 4.0, 9.0]))

    def test_GetMagnitudeOfPostiveVector(self):
        V1 = Vector([ 1.123, 4.456, 8.789 ])
        self.assertAlmostEqual( V1.magnitude() , 9.918, places=3)

    def test_GetMagnitudeOfNegativeVector(self):
        V1 = Vector([ 1.123, -4.456, 8.789 ])
        self.assertAlmostEqual( V1.magnitude() , 9.918, places=3)

    def test_GetDirectionOfPostiveVector(self):
        V1 = Vector([ 1.123, 4.456, 8.789 ])
        self.assertEqual( V1.direction().round(3) , Vector([0.113, 0.449, 0.886]))

    def test_DirectionVectorHasUnitMagnitude(self):
        V1 = Vector([ 1.123, 4.456, 8.789 ])
        self.assertEqual( V1.direction().magnitude() , 1.0)

    def test_GetDirectionOfNegativeVector(self):
        V1 = Vector([ 1.123, -4.456, 8.789 ])
        self.assertEqual( V1.direction().round(3) , Vector([0.113, -0.449, 0.886]))

    def test_DirectionVectorHasUnitMagnitude(self):
        V1 = Vector([ 1.123, 4.456, 8.789 ])
        self.assertEqual( V1.direction().magnitude() , 1.0)

    def test_AngleBetweenTwoVectorsInRadians(self):
        V1 = Vector([1.1, 2.2, 3.3])
        V2 = Vector([4.4, 5.5, 6.6])
        self.assertAlmostEqual( V1.angle( V2 ), 0.2257, places=4 )

    def test_AngleBetweenTwoVectorsInDegrees(self):
        V1 = Vector([1.1, 2.2, 3.3])
        V2 = Vector([4.4, 5.5, 6.6])
        self.assertAlmostEqual( V1.angle( V2, radians=False ), 12.933, places=3 )


    
if __name__ == '__main__':
    unittest.main()