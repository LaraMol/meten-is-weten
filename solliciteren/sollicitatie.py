def sollicitatie(question):
    Answer = input(question)

    if Answer == "J":
        return True
    elif Answer =="N":
        return sollicitatie(question)
    else:
        print ("Dat was helaas geen optie")
        return sollicitatie(question)


if sollicitatie ("Bent u klaar voor de sollicitatie J/N "):
    print ("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
Start van de sollicitatie                               +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Een ogenblikje alsublieft de volgende vragen worden gegenereerd """)

ask = input ("\nHeeft u raktijkervaring met dieren-dressuur \nOf ervaring met jongleren\nOf praktijkervaring met acrobatiek J/N ")
if ask == "J":
    ask1 = input ("\nWelke van de overstaande praktijk ervaringen heeft u en hoeveel jaar? ")
    print ("oh dat is geweldig")
    print ("dankuwel voor uw antwoord")
else:
    print("\nOke, dankuwel voor uw antwoord")

askquestion5 = input("heeft u een mbo diploma heeft u? J/N ")
if askquestion5 == "J":
    askquestion1 = input ("Welke mbo niveau diploma bevat u? ")
    print ("Fijn om te weten")
else:
    print("Oke")
question1 = input("\nIn bezit van een geldig Vrachtwagen rijbewijs J/N ")
print ("Top!")

if sollicitatie("\nbezit van een hoge hoed J/N "):
    print (" Fijn om te weten")

question3 = input("\nIs man EN heeft een snor OF is vrouw EN draagt rood krulhaar haar J/N ")
ask1 = input ("Welke van de bovenstaande bent u en hoeveel cm is ur snor/haar ")
print ("top dankuwel")

question4 = input("\nHoelang bent u ")
print ("Oke dankuwel")

question5 = input("\nHoe zwaar bent u? ")
print ("Top bedankt!")

question6 = input ("Heeft u een Certificaat Overleven met gevaarlijk personeel J/N ")
if question6 == "J":
    print ("Dat is geweldig")
elif question6 == "N":
    print ("Dankuwel")

if sollicitatie("Heeft u huisdieren? J/N "):
    print ("Oh geweldig")

if sollicitatie ("Speelt u minecraft? J/N "):
    print("Hmmm")

if sollicitatie ("Is de aarde plat? J/N "):
    print ("Oke oke")

if sollicitatie ("Ben ik cool? J/N "):
    print ("Oke ")

say = input ("Dit was de sollicitatie die u zojuist heeft gemaakt. \n Alle antwoorden zijn naar onze administratie door gestuurd kunt u asljeblieft uw email in voeren zodat u een bevestiging ontvangt.\n ")

print ("\n U hoort zo spoedig mogelijk van ons!")