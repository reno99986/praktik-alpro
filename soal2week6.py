print("\033[34m ..::Program Menghitung Bilangan Fibonacci::..")
print("\033[33m ..::Kelompok 8::..")
banyak_bilangan=int(input("Masukan angka ="))
n1 = 1 
n2 = 1

list_fibonaci = []
for count in range (1,banyak_bilangan+1):
    list_fibonaci.append(n1)
    bilangan_terakhir=n1+n2
    n1=n2
    n2=bilangan_terakhir

print(list_fibonaci)
