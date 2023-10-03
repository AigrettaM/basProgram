#List (memungkinkan duplikasi)
"""a = ["apel", "jeruk", "ceri", "durian", "apel"]
a = ["apel", "Jeruk", "ceri", 20, "apel", True, 10.2, ["mamang", "mbak"]]
b = ["sirsak", "semangka"]
a.insert(3,"semangka") #untuk menambahkan element sesuai dengan index yg diinginkan
a[2] = "manggis" # untuk mengubah element sesuai index yg diinginkan
a.append("sirsak") # append digunakan untuk menambahkan 1 elemen
a.append(b)
a.pop(3)"""

""" print(len(a))
print(a[2])
print(a[1:4]) # list untuk memanggil index awal dan akhir
print(a[1:]) # list untuk memanggil index awal dan akhir
print(a[10]) >> List index out of range
a.extend(b) # untuk menambahkan element yang lebih dari 1
print(a)
a.sort()
print(a)"""

# Tuple >> untuk mengubah, menghapus, menambah maka harus ubah konversi tipe data ke list
"""a = ("apel", "jeruk", "ceri", "durian", "apel")
x = list(a)
x[3] = "melon"
a = tuple(x)
print(a)"""

# packing dalam tuple
"""buah = ("apel", "belimbing", "ceri", "durian", "anggur")
(a, b, c, d, e) = buah
print(a)
print(b)
print(c)
print(d)
print(e)
"""
a = ["apel", "jeruk", "ceri", "durian", "apel"]
a.reverse()
print(a)