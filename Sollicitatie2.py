#Sollicitatie

from tokenize import Name


name = input("Wat is uw naam? : ")
if name == "Timo":
    raise NameError("Sorry er is geen plaats voor een 'Timo'")

gewicht = int(input("Hoe zwaar bent u? : "))
if gewicht > 95:
    raise  ValueError("U bent veeeeeeeeeeeeeeeeeeeeeel te zwaar")

nogmaals = input("Nogmaals heet u Timo? : ")
if nogmaals == "ja":
    raise NameError("Ik zei toch Timo opdonderen")




def main():
    if float(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? : ")) <= 4:
        if float(input("Hoeveel jaar ervaring heeft u met jongleren? : ")) <= 5:
            if float(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek : ")) <= 3:
              return False

    if input("Bent u in het bezit van een MBO-4 diploma? (J/N) : ") != "J": 
       return False

    if input("Bent u in het bezit van een geldig Vrachtwagen bewijs? (J/N) : ") != "J":
       return False

    if input("Heeft u een hogehoed in bezit? (J/N) : ") != "J":
       return False

    if input("Bent u een (MAN/VROUW) ? : ") == "MAN":
        if float(input("Hoe breed is uw snor? : ")) <= 10:
            return False
    else:
        if input("Heeft u rood krullend haar? (J/N) : ") != "J":
            return False
        if float(input("Hoeveel cm is uw haar? : ")) <= 20:
            return False

    if float(input("Hoeveel cm lang bent u? : ")) <=150:
        return False
    
    if input("Heeft u een certificaat overleven met gevaarlijk personeel (J/N) :") != "J":
        return False



    return True

if __name__ == "__main__":
    if main():
        print("U bent geschikt voor de baan bel het nummer 06-11 de rest komt vanzelf!!")
    else:
        print("Je bent niet geschikt voor de baan!")
print("-------------------------------------------------------------------")
