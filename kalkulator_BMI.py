wzrost=float(input("Ile masz wzrostu?\n"))
waga=float(input("Ile wazysz?\n"))
BMI = waga / (wzrost ** 2)

print("Twoje bmi wynosi: {:.1f}".format(BMI))

if (BMI<18.5):
    print("Niedowaga")
elif (BMI>=18.5 and BMI<=24):
    print("Waga normalna")
elif (BMI>24 and BMI<=26.5):
    print("Lekka nadwaga")
else:
    print("Nadwaga")
    if(30>=BMI>35):
        print("Otylosc I stopnia")
    elif(35<=BMI>40):
        print("Otylosc II stopnia")
    else:
        print("Otylosc III stopnia")
