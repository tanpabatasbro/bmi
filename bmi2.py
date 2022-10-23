berat = int(input("masukkan berat badan anda (kg):"))
tinggi = float(input("masukkan tinggi badan anda (m) :"))
BMI = berat / (tinggi * tinggi)

print("bmi anda adalah :", BMI)
if (BMI<17.0) :
    print("kurus, kekurangan berat badan tingkat berat")
elif (BMI>= 17.0 and BMI<=18.4) :
    print("kurus, kekurangan berat badan tingkat ringan")
elif (BMI>=18.5 and BMI<=25.0) :
    print("normal")
elif (BMI>=25.1 and BMI <=27.0) :
    print("gemuk, kelebihan berat badan tingkat ringan")
else:
    print("obesitas")
