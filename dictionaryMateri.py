# Dictionary untuk menyimpan data dengan format key(kata kunci) & value(nila)
# ordered, changeable, do not allow duplicated
# keys dan valuenya berurutan
# tidak bisa di duplikat, namun value bisa memiliki data yang sama
# Jika key yang sama, maka value yang akan disimpan maka yang terakhir di inputkan 

kucing = {
    "nama" : "Pipiw",
    "umur" : "Udah meninggal",
    "ras" : "persian",
    "jantan " : True,
    "hobi" : ["makan", "tidur"]
}
"""orang = {
    "nama" : "Adwa",
    "umur" : 18,
    "ras" : "sunda",
    "jantan " : False,
    "hobi" : ["mukul orang", "tidur"]
}"""
# print(orang)
# print(orang["hobi"]) # untuk mengakses item didalam suatu variabel
# print(len(orang)) # >> menghitung key nya bukan valuenya

# buah = dict(nama = "apel", 
#             warna = "Merah", 
#             manis = True)
# print(buah)

print(kucing["nama"])
print(kucing.get("ras")) # untuk mengakses item didalam suatu variabel dengan method get()
