#pizzaCalculator Upgrade

prijssmallpizza = 6  
prijsmediumpizza = 9
prijslargepizza = 13.5
prijssictergitlanpizza = 20

Continue = True

while Continue:
      try:
            Invoer1 = int(input("Hoeveel small Pizza's wilt u? : "))
            aantalsmallPizzas = Invoer1
            Invoer2 = int(input("Hoeveel medium Pizza's wilt u? : "))
            aantalmediumpizzas = Invoer2
            Invoer3 = int(input ("hoeveel large Pizza's wilt u? : "))
            aantallargepizzas = Invoer3
            Invoer4 = int(input("hoeveel sictergitlan pizza's wilt u? : "))
            aantalsictergitlanpizzas = Invoer4

            totaalprijs = Invoer1 * prijssmallpizza + Invoer2 * prijsmediumpizza + Invoer3 * prijslargepizza + Invoer4 * prijssictergitlanpizza
      except ValueError:
            print("De invoer was niet juist")
      except:
            print("Er ging iets fout.....")
      finally:
            Invoer = input("Wilt u opnieuw een aantal pizza's invullen? (ja/nee) : ")
            if Invoer =='nee':
                  Continue = False




print(f"{Invoer1}x small pizza's : (€{prijssmallpizza*Invoer1} : ")
print(f"{Invoer2}x medium pizza's : (€{prijsmediumpizza*Invoer2} : ")
print(f"{Invoer3}x large pizza's : (€{prijslargepizza*Invoer3} : ")
print(f"{Invoer4}x sictergitlan pizza's : (€{prijssictergitlanpizza*Invoer4} : ")



print(" bij de domilan kosten de pizza's " + str(totaalprijs) + "€ voor de " + str(Invoer1)
      + " small pizza's, " + str(Invoer2) + " medium pizza, " +   str(Invoer3)  + " large pizza's en de " + str(Invoer4) + " sictergitlan pizza ")

