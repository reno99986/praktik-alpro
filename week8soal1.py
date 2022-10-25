i = input("Program membalik string dan menghitung huruf vokal\nMasukkan kalimat: ")
l = i[::-1]
hvokal = ["a","i","u","e","o","A","I","U","E","O"]
jumvokal = 0
print("Kalimat aslinya adalah: ",i)
print("Kalimat yang telah dibalik adalah: ",l)
for vokal in i:
    if vokal in hvokal:
        jumvokal += 1
print("Jumlah Huruf vokal dalam kalimat adalah: ",jumvokal)
