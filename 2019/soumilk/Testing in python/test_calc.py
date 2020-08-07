import unittest
import Calculations as c

class TestCalc(unittest.TestCase):

       def test_1(self):
              self.assertEqual(c.add(10,5),15)
              self.assertEqual(c.multiply(-1,1),-1)
              self.assertEqual(c.subtract(0,5),6)
              self.assertEqual(c.divide(0,5),0)
              self.assertEqual(c.divide(5,0),6)

       def test_2(self):
              self.assertNotEqual(c.add(10,5),1)
              self.assertNotEqual(c.multiply(-1,1),-1)
              self.assertNotEqual(c.subtract(0,5),6)
              self.assertNotEqual(c.divide(0,5),0)
              self.assertNotEqual(c.divide(5,0),6)
              

if __name__=='__main__':
       unittest.main()
       

              
