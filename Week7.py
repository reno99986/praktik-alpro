print("Program Toko Tronjol 69")
Toko_barang = {
    1:"Telur",
    2:"Teh",
    3:"Roti",
    4:"Mie" ,
    5:"Kopi",
    6:"Krupuk"
}
Toko_harga = {
    "Telur" : 2000,
    "Teh" : 70000,
    "Roti" : 5000,
    "Mie" : 3000,
    "Kopi" : 2000,
    "Krupuk" : 8000
}
Toko_stok = {
    "Telur" : 69,
    "Teh" : 69,
    "Roti" : 69,
    "Mie" : 69,
    "Kopi" : 69,
    "Krupuk" : 69
}
print("1.Beli\n2.Edit jumlah Barang\n3.Edit harga barang\n4.Tambah Barang\n5.Keluar")
def daftar():
    for x in Toko_barang:
        print(f"{x}.{Toko_barang[x]}\t\t stok:{Toko_stok[Toko_barang[x]]}\t\t harga:{Toko_harga[Toko_barang[x]]}")
def beli():
    x=  int(input("Barang apa yang ingin dibeli? "))
    if x in Toko_barang.keys():
        bar = Toko_barang[x]
        y= int(input("Berapa jumlah yang ingin dibeli? "))
        ang= Toko_harga[bar]
        stok= Toko_stok[bar]
        sisa = stok - y
        if sisa >=0:
            jumlah = ang * y
            print(f"Total {Toko_barang[x]} yang ingin dibeli adalah {y}, Jumlah yang harus dibayar adalah Rp.{jumlah}")
            input("Enter untuk Lanjutkan")
            print("Terimakasih Telah Berbelanja di Toko kami!")
            Toko_stok.update({bar: sisa})
            daftar()
        else:
            print("Maaf, kami tidak memiliki stok yang cukup")
    else:
        print("Masukkan Item Yang Benar")
def editharga():
    x= int(input("Barang apa yang harganya ingin di edit? "))
    y= Toko_barang[x]
    harga= int(input("Masukkan Harga Barang Yang baru: Rp."))
    if harga >=0:
        Toko_harga.update({y:harga})
        print("Harga baru: ")
        daftar()
    else:
        print("Yakali harga negatif")
def editstok():
    x= int(input("Barang apa yang stoknya ingin di edit? "))
    y = Toko_barang[x]
    stok = int(input("Masukkan Jumlah Stok Yang Baru: "))
    if stok >= 0 :
        Toko_stok.update({y:stok})
        print("Stok Baru:")
        daftar()
    else:
        print("Yakali Stok Negatif")
def ulang():
    print("\n\n1.Beli\n2.Edit jumlah Barang\n3.Edit harga barang\n4.Tambah Barang\n5.Keluar")
    global menu
    menu = int(input("Masukkan angka menu yang ingin dipilih "))
def tambahbarang():
    x= int(input("Masukkan Kode barang(1-9999): "))
    y= input("Masukkan nama barang: ")
    z= int(input("Masukkan Stok awal barang: "))
    ko= int(input("Masukkan harga barang: Rp."))
    Toko_barang.update({x:y})
    Toko_stok.update({y:z})
    Toko_harga.update({y:ko})
menu = int(input("Masukkan angka menu yang ingin dipilih "))
while menu >0 and menu<5:
    daftar()
    if menu == 1:
        beli()
        ulang()
    elif menu == 2:
        editstok()
        ulang()
    elif menu == 3:
        editharga()
        ulang()
    else:
        tambahbarang()
        ulang()
print("See you next time~")
# Ini Cuman Komen Gabut Biar Pas 100 Line
# Orang-Orang Kok bisa sampe lebig 100 yaa
# Kok kode saya cuman 100 line jadi insekyur
#...........................................#