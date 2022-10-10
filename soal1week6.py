print("\033[36m ..::Program Menghitung Derek Harmonik::..")
print("\033[32m ..::Kelompok 8::..")
i = int(input("Masukkan Inoutan untuk deret harmonik: "))
j= 0
jabar = ""
for x in range(1,i+1):
    j += 1/x
    if x == 1:
        jabar += "1+"
    elif x < i and x > 1 :
        jabar += f"1/{x}+"
    else:
        jabar += f"1/{x}="
print(jabar,j)
