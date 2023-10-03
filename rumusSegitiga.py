"""# Flowchart rumus
alas =int(input("Masukkan alas segitiga: "))
tinggi = int(input("Masukan tinggi segitiga: "))
luas =int(alas*tinggi/2)

print("======================================================\n")
print(luas)"""


# Flowchart habis dibagi 3
"""angka = int(input("Masukkan bilangan: "))
hasil = angka %3 == 0
print("======================================================\n")
if hasil - False :
    print("Bilangan ini habis dibagi 3")"""


# Flowchart Kelulusan
"""bilangan = int(input("Masukkan nilai anda >> "))
if(bilangan) <= 60:
    print("Anda TIDAK LULUS".format(bilangan))
else:
    print("Anda LULUS".format(bilangan))
print("======================================================\n")"""


# Flowchart Ganjil Genap
"""angkaGG = int(input("Masukkan Angka >> "))

if(angkaGG % 2) == 0:
    print("{0} merupakan bilangan genap".format(angkaGG))
else:
    print("{0} merupakan bilangan ganjil".format(angkaGG))
print("======================================================\n")"""

# Biodata
"""nama = str(input("Masukkan Nama Anda : "))
umur = int(input("Masukkan Umur Anda : "))
print("======================================================\n")
print(f"Selamat datang {nama}!, Umur Anda sekarang adalah {umur} tahun")"""

# Kalkulator
"""print("======================================================\n")
print("Operasi Matematika")
print(" 1. Tambah \t [+]")
print(" 1. Kurang \t [-]")
print("======================================================\n")
operasi = input("Pilih Operasi (1/2)")
if operasi == '1':
  print("Kamu memilih penjumlahan")
elif operasi == '2':
  print("User memilih pengurangan")
else :
  print("Tidak valid")
print("======================================================\n")
bilangan1 = int(input("Masukkan bilangan pertama : "))
bilangan2 = int(input("Masukkan bilangan kedua : "))

if operasi == '1':
  hasil = bilangan1 + bilangan2
  print(f"Hasil operasi dari {bilangan1} + {bilangan2} = {hasil}")
elif operasi == '2':
  hasil = bilangan1 - bilangan2
  print(f"Hasil operasi dari {bilangan1} - {bilangan2} = {hasil}")
else:
  print("Tidak valid")"""

# Program Lahir tahun
nama = str(input("Masukkkan nama Anda >> "))
tahunLhr = int(input("Masukkan tahun lahir Anda >> "))
tahunSkrng = 2023
umur = tahunSkrng - tahunLhr
print("======================================================")
print(f"Selamat datang {nama}!, Umur anda saat ini {umur} tahun")
