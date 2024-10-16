import unittest
from HitungHuruf import hitung_huruf

# ! Cara run Python test: python -m unittest Test_HitungHuruf.py

class TestHitungHuruf(unittest.TestCase):

    def test_huruf_biasa(self):
        """Test Case 1: Menguji fungsi dengan string biasa yang berisi huruf, spasi, dan tanda baca"""
        self.assertEqual(hitung_huruf("halo kami BLUG"), 12)  

    def test_huruf_tanpa_huruf(self):
        """Test Case 2: Menguji fungsi dengan string yang tidak mengandung huruf sama sekali"""
        self.assertEqual(hitung_huruf("1234567890"), 0)  

    def test_huruf_hanya_vokal(self):
        """Test Case 3: Menguji fungsi dengan string yang hanya berisi huruf vokal"""
        self.assertEqual(hitung_huruf("aeiouAEIOU"), 10)  

    def test_huruf_hanya_konsonan(self):
        """Test Case 4: Menguji fungsi dengan string yang hanya berisi huruf konsonan"""
        self.assertEqual(hitung_huruf("bcdfghjklmnpqrstvwxyz"), 21) 

    def test_huruf_kosong(self):
        """Test Case 5: Menguji fungsi dengan string kosong"""
        self.assertEqual(hitung_huruf(""), 0)  

    def test_huruf_spasi_dan_tanda_baca(self):
        """Test Case 6: Menguji fungsi dengan string yang berisi huruf, spasi, dan tanda baca"""
        self.assertEqual(hitung_huruf("Ini adalah contoh, dengan spasi dan tanda baca!"), 38)  

if __name__ == '__main__':
    unittest.main()
