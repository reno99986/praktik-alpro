def fungsi(x):
    y = (6 * (x ** 2)) + 3 * x + 2
    return(y)
print("Hp={",end="")
for i in range (-10,10+1,1):
    print("(",(i),",",fungsi(i),")",end="")
print("}")
