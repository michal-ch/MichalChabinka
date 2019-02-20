start=float(input("Stan początkowy konta:"))
stopa=float(input("Stopa oprocentowania w %:"))
czas=int(input("Okres lokaty w latach:"))
czas2= czas*12
tax=0.19
inflation=0.025
stopa2=stopa/100
wynik = start * ((1 + (stopa2/12)) ** (12*czas))
wynik2= (wynik-start)*tax
wynik3= (wynik-wynik2-start)*inflation
wynik4= wynik-wynik2-wynik3
wynik5= wynik4-start
print("Twoje {:.0f} zł przez {} lata na lokacie {} % urośnie do {:.2f} zł." .format(start, czas, stopa, wynik4))
print("Twoj zysku w ciagu {} miesiecy bedzie wynosil: {:.2f} zl".format(czas2,wynik5))
