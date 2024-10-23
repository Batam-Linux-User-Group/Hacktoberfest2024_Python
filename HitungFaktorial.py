"""
 * Buatlah program yang meminta input sebuah bilangan dari pengguna, 
   kemudian menghitung dan menampilkan faktorial dari bilangan
 * Contoh:
 * Input: 5
 * Output: 125
"""

# Jangan Ubah nama function
def faktorial(n):
    if n < 0: raise RecursionError("Input tidak valid. n harus bilangan positif.")
    elif n == 0 or n == 1: return 1
    else: return n * faktorial(n - 1)
