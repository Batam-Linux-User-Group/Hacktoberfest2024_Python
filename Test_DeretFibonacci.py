import unittest
from DeretFibonacci import deret_fibonacci

# ! Cara run Python test: python -m unittest Test_DeretFibonacci.py

class TestDeretFibonacci(unittest.TestCase):
    

    def test_sepuluh_bilangan(self):
        """Test Case 1 : menguji 10 bilangan Fibonacci pertama"""
        self.assertEqual(deret_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_satu_bilangan(self):
        """Test Case  2 : menguji 1 bilangan Fibonacci"""
        self.assertEqual(deret_fibonacci(1), [0])

    def test_nol_bilangan(self):
        """Test Case 3 : menguji 0 bilangan Fibonacci"""
        self.assertEqual(deret_fibonacci(0), [])

    def test_input_negatif(self):
        """Test Case 4 : menguji untuk input negatif"""
        self.assertEqual(deret_fibonacci(-5), "Input tidak valid. n harus bilangan positif.")
    
    def test_input_kosong(self):
        """Test Case 5 : menguji untuk input None (kosong)"""
        with self.assertRaises(TypeError):
            deret_fibonacci(None)

if __name__ == '__main__':
    unittest.main()
