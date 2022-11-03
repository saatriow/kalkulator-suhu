print("==========kalkulator suhu==========")
print("Pilih suhu yang ingin dirubah")
pil = int(input("1. Celcius \n2. Farenheit \n3. Reamur \n4. Kelvin \n"))
if (pil == 1):
    suhu= float(input("Masukkan Suhu celcius awal : "))
    pil2 = int(input("ubah celcius ke : \n1. Farenheit \n2. Reamur \n3. Kelvin \n"))
    if (pil2==1):
        print(suhu, "celcius = ", (9/5*suhu)+32 ,"Farenheit")
    elif(pil2==2):
        print(suhu, "celcius = ", (4/5*suhu) ,"Reamur")
    elif(pil2==3):
        print(suhu, "celcius = ", suhu + 273 ,"Kelvin")
    else:
        print("Tidak valid")
elif (pil == 2):
    suhu= float(input("Masukkan Suhu Farenheit awal : "))
    pil2 = int(input("ubah ke : \n1. Celcius \n2. Reamur \n3. Kelvin\n"))
    if (pil2==1):
        print(suhu, "Fahrenhait = ", (5/9*(suhu-32)) ,"Celcius")
    elif(pil2==2):
        print(suhu, "Fahrenhait = ", (4/9*(suhu-32)) ,"Reamur")
    elif(pil2==3):
        print(suhu, "Fahrenhait = ", (5/9*(suhu-32) + 273) ,"Kelvin")
    else:
        print("Tidak valid")
elif (pil==3):
    suhu= float(input("Masukkan Suhu Reamur awal : "))
    pil2 = int(input("ubah ke : \n1. Celcius \n2. Farenheit \n3. Kelvin\n"))
    if (pil2==1):
        print (suhu, "Reamur = ", (5/4*suhu) ,"Celcius")
    elif(pil2==2):
        print(suhu, "Reamur = ", (9/4*suhu) + 32 ,"Farenheit")
    elif(pil2==3):
        print(suhu, "Reamur = ", (5/4*suhu) + 273 ,"Kelvin")
    else:
        print("Tidak valid")
elif (pil==4):
    suhu= float(input("Masukkan Suhu Kelvin awal : "))
    pil2 = int(input("ubah ke : \n1. Celcius \n2. Farenheit \n3. reamur\n"))
    if (pil2==1):
        print (suhu, "Kelvin = ", suhu - 273 ,"Celcius")
    elif(pil2==2):
        print(suhu, "Kelvin = ", (9/5*(suhu-273)+32) ,"Farenheit")
    elif(pil2==3):
        print(suhu, "Kelvin = ", (4/5*(suhu-273)) ,"reamur")
    else:
        print("Tidak valid")
else:
    print("tidak valid")
