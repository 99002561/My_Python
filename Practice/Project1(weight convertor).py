User_weight=input("Weight: ")
LorK=input("Lbs_or_Kg: ")
if LorK == 'l':
    a=int(User_weight)*0.45
    print(f"You are {a} kilos")
else:
    b = int(User_weight) / 0.45
    print(f"You are {b} pounds")