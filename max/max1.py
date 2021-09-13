a = int(input("Geef a nu: "))
b = int(input("geef b nu: "))

if a>b:
    max = a
    min = b
    print("a is het grootste getal" + str(max))
elif b>a:
    max = b
    min = a
    print ("a is het kleinst getal" + str(min))
    
else:
    print ("a en b zijn even groot")
