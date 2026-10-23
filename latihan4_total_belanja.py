nama_barang = str(input("masukkan nama barang : "))
harga_barang = int(input("masukkan harga barang : "))
jumlah_barang = int(input("masukkan jumlah barang : "))

subtotal = harga_barang * jumlah_barang
ppn_11 =  subtotal * 0.11
total = subtotal + ppn_11

print(f"subtotal : {subtotal}")
print(f"ppn 11% : {ppn_11}")
print(f"total : {total}")


