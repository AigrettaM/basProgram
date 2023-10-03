# sifat set unordered, tidak akan menyimpan item yang sama

a = {"apel", "jeruk", "ceri", "durian"}
b = {"strawberry", "blueberry", "apel"}
# a = {"apel", "jeruk", "ceri", "durian", "apel"} # tipe data set sifatnya tidak berurutan / unordered, walaupun tipe datanya berbeda
# a = {"apek", "jeruk", 20, True, "durian", 9.7} # tipe  data set tidak memiliki index, maka untuk mengakses item set harus menggunakan if atau loop
# print(a) 

# for item in a:
#     print(item)

# print("jeruk" in a)
# print("pisang" in a)

# a.update(b)
# print(a)

# a.add("semangka") # sama seperti irisan pada matematika
# print(a)

# c = a.union(b) # bersifat harus dengan variabel atau menyimpan di variabel , sama seperti irisan pada matematika
# print(c)

# a.intersection_update(b) # untuk menyimpan variabel yang nilainya sama saja
# print(a)

# c = a.intersection(b) # fungsi yang sama namun berbeda dengan penyimpanan nilai di dalam variabel c, sama seperti irisan pada matematika
# print(c)

# a.symmetric_difference_update(b) # tidak ada nilai yang sama divariabel, tidak perlu membuat variabel baru
# print(a)

# c = a.symmetric_difference(b) # tidak ada nilai yang sama divariabel, namun bedanya hanya dimasukkan ke variabel baru
# print(c)

# a.update(b)
# print(a)

# b.update(a)
# print(b)

# a.pop() # useless, lebih baik mengubah pake list
# print(a)

# a.clear()
# print(a)