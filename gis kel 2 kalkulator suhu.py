print("Selamat Datang di Program Konversi Suhu")
print("========== KALKULATOR SUHU GIS 2 ==========")
print("Silahkan pilih suhu yang ingin dirubah")
pil = int(input("1. Celcius \n2. Fahrenheit \n3. Reamur \n4. Kelvin \n"))
if (pil == 1):
    suhu= float(input("Masukkan Suhu Awal Celcius : "))
    pil2 = int(input("ubah celcius ke : \n1. Fahrenheit \n2. Reamur \n3. Kelvin \n"))
    if (pil2==1):
        print(suhu, "celcius = ", (9/5*suhu)+32 ,"Fahrenheit")
    elif(pil2==2):
        print(suhu, "celcius = ", (4/5*suhu) ,"Reamur")
    elif(pil2==3):
        print(suhu, "celcius = ", suhu + 273 ,"Kelvin")
    else:
        print("Tidak valid")
elif (pil == 2):
    suhu= float(input("Silahkan Masukkan Suhu Awal Fahrenheit : "))
    pil2 = int(input("ubah ke : \n1. Celcius \n2. Reamur \n3. Kelvin\n"))
    if (pil2==1):
        print(suhu, "Fahrenheit = ", (5/9*(suhu-32)) ,"Celcius")
    elif(pil2==2):
        print(suhu, "Fahrenheit = ", (4/9*(suhu-32)) ,"Reamur")
    elif(pil2==3):
        print(suhu, "Fahrenheit = ", (5/9*(suhu-32) + 273) ,"Kelvin")
    else:
        print("Tidak valid")
elif (pil==3):
    suhu= float(input("Silahkan Masukkan Suhu Awal Reamur : "))
    pil2 = int(input("ubah ke : \n1. Celcius \n2. Fahrenheit \n3. Kelvin\n"))
    if (pil2==1):
        print (suhu, "Reamur = ", (5/4*suhu) ,"Celcius")
    elif(pil2==2):
        print(suhu, "Reamur = ", (9/4*suhu) + 32 ,"Fahrenheit")
    elif(pil2==3):
        print(suhu, "Reamur = ", (5/4*suhu) + 273 ,"Kelvin")
    else:
        print("Tidak valid")
elif (pil==4):
    suhu= float(input("Silahkan Masukkan Suhu Awal Kelvin : "))
    pil2 = int(input("ubah ke : \n1. Celcius \n2. Fahrenheit \n3. Reamur\n"))
    if (pil2==1):
        print (suhu, "Kelvin = ", suhu - 273 ,"Celcius")
    elif(pil2==2):
        print(suhu, "Kelvin = ", (9/5*(suhu-273)+32) ,"Fahrenheit")
    elif(pil2==3):
        print(suhu, "Kelvin = ", (4/5*(suhu-273)) ,"Reamur")
    else:
        print("Maaf Tidak valid")
else:
    print("Tidak valid")
