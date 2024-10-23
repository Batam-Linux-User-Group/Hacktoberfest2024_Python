"""
 * Buatlah fungsi yang menghitung jumlah huruf dalam sebuah string.
 * Contoh:
 * Input: halo kami BLUG
 * Output: 12
"""

# Jangan Ubah nama function
def hitung_huruf(string):
    return len([i for i in string if i.isalpha()])
