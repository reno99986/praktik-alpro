campur = input("Masukkan String: ")
def angka():
    ang = ""
    alp = ""
    sym = ""
    campur.strip()
    for x in campur:
        if x.isdigit():
            ang += x
        elif x.isalpha():
            alp +=x
        else:
            sym+=x
    return [alp,int(ang),sym]
print(angka())
