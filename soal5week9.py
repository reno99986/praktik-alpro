def fungsi(a,b):
    jum = 0
    jab = ""
    while a <= b:
        if a % 2 == 0:
            if a <= b-2:
                jab += f"{a}+"
                jum+=a
                a += 2
            else:
                jab += f"{a}="
                jum+=a
                a += 2
        else:
            a += 1
    semua=jab+str(jum)
    return(semua)
p=int(input("Masukkan angka awal: "))
r=int(input("Masukkan angka akhir: "))
print(fungsi(p,r))
