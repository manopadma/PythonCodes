#Hotel Room Booking using Nested If

print("Welcome to Tasty Briyani")
Print("1.Chicken")
Print("2.Mutton")
Print("3.Beef")
Print("4.plain")

custumer = int(input("Enter ur Choice of Briyani"))
costPrice = 0
chicken = 100
mb = 120
bb = 130
briyani = 70
egg = 10
omballete =25


if custumer == 1:
    print("Your Choice is Chicken  Briyani")
    addEgg = input("Do you want Extra Egg: Y/N")
    addOmballet = input("Do you want Omballet : Y\N")
    costPrice += chicken
    if addEgg == "Y":
        costPrice += egg
        print(f"Egg Price is: ${egg}")
    if addOmballet == "Y":
        costPrice += omballete
        print(f"Omballet Price is: ${omballete}")  
    print(f"Chicken Briyani Price is:{chicken}") 
    print(f"The Total Amount is: ${costPrice}")



