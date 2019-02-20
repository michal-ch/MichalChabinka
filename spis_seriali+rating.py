seriale= {
    "Arrow":10,
    "M jak milosc":6,
    "Avengers":9,
    "Pamietniki z wakacji":5.5,
    "Kasyno":8.5,
    "Zwiadowca":9,
    "Kryminalni":8.5,
    }
print(list(seriale.keys()))
print("\n","-----------------------------------------------------","\n")
nazwa=input("Jaki serial chcesz obejrzec? ")
print("{} otrzymal u nas ocene: {}".format(nazwa,seriale[nazwa]))
print("\n","-----------------------------------------------------","\n")
new=input("Jaki serial chcialbys dodac? ")
rating=input("Jaki rating uzyskal wedlug Ciebie "+new+ "? ")
seriale[new]= float(rating)

print("\n","-----------------------------------------------------","\n")
print(list(seriale.keys()))
