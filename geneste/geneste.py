kaas1 = input ("Is de kaas geel? ")
if kaas1 == "ja":
        ask1 = input ("Zitten er gaten in? ")
        if ask1 == "ja":
                ask2 = input("Is de kaas belachelijk duur? ")
                if ask2 == "ja":
                    print("Emmenthaler")
                elif ask2 == "nee":
                    print ("Leerdammer")
                    

        if ask1 == "nee":
            ask3 = input ("Is de kaas hard als steen? ")
            if ask3 == "ja":
                print ("Parmigiano Reggiano ")
            elif ask3 == "nee":
                print ("Goudse kaas")

if kaas1 =="nee":
    ask4 = input ("Heeft de kaas blauwe schimmels? ")
    if ask4 == "ja":
        ask5 = input ("Heeft de kaas een korst? ")
        if ask5 == "ja":
            print ("Blue de Rochbaron")
        elif ask6 == "nee":
            print ("Foume d'Ambert")
    
    if ask4 == "nee":
        ask6 = input ("Heeft de kaas een korst? ")
        if ask6 == "ja":
            print("Camembert")
        elif ask6 == "nee":
            print("Mozzarella")

else:
    print ("invalid option")