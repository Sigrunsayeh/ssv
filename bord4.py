def level3(self):
    print("Þetta er borð 3.")
    print("Sæll Sigmundur, í þessu borði spilum við hengimann")
    print("Ef þér tekst ekki að finna orðið í færri en 10 tilraunum þá taparðu")
    #bidum i 1 sek
    time.sleep(1)
    print("Fyrsta gisk:"")
    time.sleep(0.5)
    ord = "panama"
    tilraunir = 10
    while tilraunir>0
    fail = 0
    gisk = input('Giskaðu á staf:')
        for char in ord:
            if char in gisk:
                print (char,)
            else:
                print "_"
                fail += 1
            if fail == 0:
                print ("Þú vannst")
                break
            if gisk not in ord:
                tilraunir -=1
                print("Ekki rétt")
                time.sleep(0.5)
                print("Þú hefur", + tilraunir, "í viðbót")
                if tilraunir ==0
                    print("Þú hefur tapað")
