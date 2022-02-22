
import math
import unittest
from circle import circle

class test_circle(unittest.TestCase):

    def setUp(self):
        
        self.circle_1 = circle(0)
        self.circle_2 = circle(1)
        self.circle_3 = circle(90)

    def test_parameters(self):
        
        self.assertEqual(self.circle_1.radius, 0)
        self.assertEqual(self.circle_2.radius, 1)
        self.assertEqual(self.circle_3.radius, 90)

        self.assertEqual(self.circle_1.parameters['Radius'], 0)
        self.assertEqual(self.circle_2.parameters['Radius'], 1)
        self.assertEqual(self.circle_3.parameters['Radius'], 90)

        self.circle_1.new_pars(1)
        self.circle_2.new_pars(2)
        self.circle_3.new_pars(3)
        
        self.assertEqual(self.circle_1.radius, 1)
        self.assertEqual(self.circle_2.radius, 2)
        self.assertEqual(self.circle_3.radius, 3)

        self.assertEqual(self.circle_1.parameters['Radius'], 1)
        self.assertEqual(self.circle_2.parameters['Radius'], 2)
        self.assertEqual(self.circle_3.parameters['Radius'], 3)

    def test_perimeter(self):
        
        self.assertAlmostEqual(self.circle_1.perimeter(), 0)
        self.assertAlmostEqual(self.circle_2.perimeter(), math.pi*2)
        self.assertAlmostEqual(self.circle_3.perimeter(), math.pi*90*2)

    def test_area(self):

        self.assertEqual(self.circle_1.area(), 0)
        self.assertEqual(self.circle_2.area(), math.pi)
        self.assertEqual(self.circle_3.area(), math.pi*90**2)
    
    def test_diameter(self):

        self.assertEqual(self.circle_1.diameter(), 0)
        self.assertEqual(self.circle_2.diameter(), 2)
        self.assertEqual(self.circle_3.diameter(), 180)

if __name__ == '__main__':

    unittest.main()



