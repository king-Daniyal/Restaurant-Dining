def menu_select():
    Pesto_pasta = "15$ : small" 
    Italian_pizza = " 10$ : small" + " 23$ : medium" + " 43$ : large "
    Coq_au_Vin = " 30 $ : medium" + " 40$ : large"
    print("Welcome to UCL bostas restaurant")
    print("We have three things on the menu")
    menu_items = ["Pesto Pasta", "Italian Pizza", "Coq au Vin"]
    print("Pesto Pasta" +", Italian Pizza, " + "Coq au Vin")
    print( " In order to get to know prices and size please pick a dish")
    text = input("Dish") 
    if text == "1":
        print(Pesto_pasta)
    if text == "2":
        print(Italian_pizza)
    print(Coq_au_Vin)
    return ("Thank you for dining with us!")
    
print(menu_select())
    
