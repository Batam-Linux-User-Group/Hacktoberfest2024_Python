
import unittest
from HitungFaktorial import faktorial

# ! Cara run Python test: python -m unittest Test_HitungFaktorial.py

class TestFaktorial(unittest.TestCase):

    """Test Case 1 : menguji faktorial"""
    def test_faktorial_0(self):
        self.assertEqual(faktorial(0), 1)  

    """Test Case 2 : menguji faktorial 2"""
    def test_faktorial_1(self):
        self.assertEqual(faktorial(1), 1)  

    """Test Case 3 : menguji faktorial negatif"""
    def test_faktorial_negative(self):
        with self.assertRaises(RecursionError):  
            faktorial(-1)

if __name__ == '__main__':
    unittest.main()
