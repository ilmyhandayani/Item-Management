stokBarang = []
barang = {}
ulang = True

def menu():
    print()
    print("========== Menu Stok Barang ==========")
    print("1. Input barang")
    print("2. Lihat semua barang")
    print("3. Cari barang")
    print("4. Ubah barang by nomor")
    print("5. Hapus barang by nomor")
    print("6. Keluar")
    print("=======================================")
    print()

def cek_no(panjang, nomor):
    nilai = 0
    for i in range(panjang):
        if nomor == stokBarang[i]["no_barang"]:
            nilai = 1
    return nilai

def input_barang():
    no_barang = int(input("Masukkan nomor barang : "))
    nama_barang = input("Masukkan nama barang : ")
    harga_barang = int(input("Masukkan harga barang : "))
    stok_barang = int(input("Masukkan jumlah stok : "))
    
    if cek_no(len(stokBarang), no_barang) == 0:
        tmpBarang = {"no_barang": no_barang, "nama_barang": nama_barang, "harga_barang":harga_barang, "stok_barang":stok_barang}
        barang.update(tmpBarang)
        stokBarang.append(barang.copy())
    else:
        print("PERINGATAN!!!")
        print("Nomor barang sudah ada!")
        input("press enter to continue...")

def lihat_barang(panjang, data):
    if (len(stokBarang) == 0):
        print("Barang Masih Kosong")

    else:
        for i in range(panjang):
            print("Barang ke ", str(i+1))
            for key, value in data[i].items():
                print(key,":", value)	
        print()
    input("Press enter to continue ...")

def cari_barang(panjang, nama_barang, data):
    for i in range(panjang):
        if nama_barang == stokBarang[i]["nama_barang"]:
            for key, value in data[i].items():
                print(key, ":", value)
        else:
            print()
    input("press enter to continue...")

def ubahData_barang(nomor_barang):
    noBarang_baru = nomor_barang
    namaBarang_baru = str(input("Masukan nama barang yang baru:"))
    hargaBarang_baru = int(input("Masukan harga barang yang baru:"))
    stokBarang_baru = int(input("Masukan stok barang baru:"))
    dataBarang_baru = {"no_barang" : noBarang_baru, "nama_barang" : namaBarang_baru, "harga_barang" : hargaBarang_baru, "stok_barang" : stokBarang_baru}
    barang.update(dataBarang_baru)
    stokBarang.append(barang.copy())
    print("Data Berhasil Diubah")
    input("\nTekan Enter Untuk Melanjutkan...")

def hapus_barang(nomor_barang):
    for barang in range(len(stokBarang)):
        if stokBarang[barang]["no_barang"] == nomor_barang:
            del stokBarang[barang]
            print("Berhasil dihapus")
            input("Tekan Enter Untuk Melanjutkan...")
        else:
            print("")
            input()


def keluar():
    print("-----Anda Telah Keluar-----")

while ulang:
    menu()
    pilihan = int(input("Masukkan pilihan anda : "))
    if pilihan == 1:
        input_barang()
    elif pilihan == 2:
        lihat_barang(len(stokBarang), stokBarang)
    elif pilihan == 3:
        nama_barang = input("Masukan Nama Barang : ")
        cari_barang(len(stokBarang), nama_barang, stokBarang)
    elif pilihan == 4:
        nomorBarang = int(input("Masukan Nomor Barang:"))
        ubahData_barang(nomorBarang)
    elif pilihan == 5:
        hapus = int(input("Masukan Nomor Barang:"))
        hapus_barang(hapus)
    elif pilihan == 6:
        print("Anda Telah Keluar")
        ulang = False


print("\nTerimakasih")