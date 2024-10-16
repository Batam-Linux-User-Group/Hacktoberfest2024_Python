import unittest
from CekBilanganPrima import cek_bilangan_prima 

# ! Cara run Python test: python -m unittest Test_CekBilanganPrima.py

class TestCekBilanganPrima(unittest.TestCase):

    def test_bilangan_prima(self):
        """Test Case 1: Menguji beberapa bilangan prima"""
        self.assertTrue(cek_bilangan_prima(2))    
        self.assertTrue(cek_bilangan_prima(3))    
        self.assertTrue(cek_bilangan_prima(5))   
        self.assertTrue(cek_bilangan_prima(7))   
        self.assertTrue(cek_bilangan_prima(11))  
        self.assertTrue(cek_bilangan_prima(13))  
        self.assertTrue(cek_bilangan_prima(17))  
        self.assertTrue(cek_bilangan_prima(19))  
        self.assertTrue(cek_bilangan_prima(29))  
        self.assertTrue(cek_bilangan_prima(97))   

    def test_bukan_bilangan_prima(self):
        """Test Case 2: Menguji beberapa bilangan yang bukan prima"""
        self.assertFalse(cek_bilangan_prima(1))   
        self.assertFalse(cek_bilangan_prima(0))    
        self.assertFalse(cek_bilangan_prima(-5))  
        self.assertFalse(cek_bilangan_prima(4))   
        self.assertFalse(cek_bilangan_prima(10))   
        self.assertFalse(cek_bilangan_prima(100)) 
        self.assertFalse(cek_bilangan_prima(51))  

    def test_bilangan_negatif(self):
        """Test Case 3: Menguji bilangan negatif yang seharusnya bukan bilangan prima"""
        self.assertFalse(cek_bilangan_prima(-7))  
        self.assertFalse(cek_bilangan_prima(-11))  
        self.assertFalse(cek_bilangan_prima(-29))  

    def test_bilangan_besar(self):
        """Test Case 4: Menguji bilangan besar yang diketahui prima dan bukan prima"""
        self.assertTrue(cek_bilangan_prima(7919))   
        self.assertFalse(cek_bilangan_prima(8000))  

if __name__ == '__main__':
    unittest.main()
