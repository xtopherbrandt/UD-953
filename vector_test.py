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

    def test_VectorIsParallelToItself(self):
        V1 = Vector([1.,2.,3.])
        self.assertTrue( V1.isParallel(V1) )

    def test_VectorIsParallelToNegativeOfItself(self):
        V1 = Vector([1.,2.,3.])
        self.assertTrue( V1.isParallel(V1 * -1) )       

    def test_VectorIsParallelToAMultipleOfItSelf(self):
        V1 = Vector([1.,2.,3.])
        self.assertTrue( V1.isParallel(V1 * 2) ) 

    def test_VectorIsNotParallelToANonMultipleofItself(self):
        V1 = Vector([1.,2.,3.])
        V2 = Vector([2.,3.,4.])
        self.assertFalse( V1.isParallel( V2 ) )

    def test_VectorIsOrthogonalToZerovector(self):
        V1 = Vector([1.,2.,3.])
        self.assertTrue( V1.isOrthogonal(Vector.Zero( 3 )) )

    def test_VectorIsOrthogonalToAnOrthogonalVector(self):
        V1 = Vector([1.,2.])
        V2 = Vector([1.,-0.5])
        self.assertTrue( V1.isOrthogonal(V2) )

    def test_VectorIsNotOrthogonalToAParallelVector(self):
        V1 = Vector([1.,2.,3.])
        self.assertFalse( V1.isOrthogonal(V1 * 2) )

    def test_ProjectionOfVOnB(self):
        V = Vector([1.,2.,3.])
        B = Vector([3.,4.,5.])
        self.assertEqual( B.proj(V).round(3), Vector([1.56, 2.08, 2.60]))

    def test_VParallelToB(self):
        V = Vector([1.,2.,3.])
        B = Vector([3.,4.,5.])
        self.assertEqual( V.parallelTo(B).round(3), Vector([1.56, 2.08, 2.60]))
    
    def test_VPerpendicularToB(self):
        V = Vector([1.,2.,3.])
        B = Vector([3.,4.,5.])
        self.assertEqual( V.perpendicularTo(B).round(3), Vector([-0.56, -0.08, 0.40]))

    def test_VPerpPlusVParallelEqualV(self):
        V = Vector([1.,2.,3.])
        B = Vector([3.,4.,5.])
        self.assertEqual( V.perpendicularTo(B) + V.parallelTo(B), V )
                
    def test_VCrossWIsPerpendicularToV(self):
        V = Vector([1.,2.,3.])
        W = Vector([3.,4.,5.])
        self.assertTrue( V.cross(W).perpendicularTo(V) )
                
    def test_VCrossWIsPerpendicularToW(self):
        V = Vector([1.,2.,3.])
        W = Vector([3.,4.,5.])
        self.assertTrue( V.cross(W).perpendicularTo(W) )
                        
    def test_VCrossWIsNegativeWCrossV(self):
        V = Vector([1.,2.,3.])
        W = Vector([3.,4.,5.])
        self.assertEqual( V.cross(W), W.cross(V) * -1 )
                
    def test_VCrossWIsCorrect(self):
        V = Vector([1.,2.,3.])
        W = Vector([3.,4.,5.])
        self.assertEqual( V.cross(W).round(3), Vector([-2.,4.,-2.]) )


if __name__ == '__main__':
    unittest.main()