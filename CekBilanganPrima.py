"""
 * Buat fungsi yang memeriksa apakah sebuah angka merupakan bilangan prima.
 * Contoh:
 * Input: 7
 * Output: True
"""


# Jangan Ubah nama function
def cek_bilangan_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False    
    return True
