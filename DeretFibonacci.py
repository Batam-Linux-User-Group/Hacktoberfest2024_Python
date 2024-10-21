"""
 * Buatlah program yang menghasilkan deret Fibonacci hingga n bilangan, di mana n ditentukan dalam kode. 
   Program harus menghitung deret Fibonacci dan menampilkannya dalam bentuk list.
 * Contoh:
 * Input: 10
 * Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""


# Jangan Ubah nama function
def deret_fibonacci(n):
    if n < 0:
        return "Input tidak valid. n harus bilangan positif."
    fib_sequence = [0, 1] 
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

