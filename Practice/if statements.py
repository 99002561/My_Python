is_hot= True
is_cold=False
if is_hot: #will be ignored
    print("It's a hot day")
    print("drink water")
elif is_cold:
    print("It is a cold day")
else:
    print("It is a lovely day")
print("Enjoy your day")


is_hot= False
if is_hot:
    print("It's a hot day")
print("Enjoy your day") #Enjoy your day

is_hot= False
if is_hot:
    print("It's a hot day")
    print("drink water")
else:
    print("It is a cold day")
print("Enjoy your day")

#exercise
price=1000000
Good_credit=True
if Good_credit:
    Downpayment= 0.1*price
else :
    Downpayment=0.2 * price
#print(f'Down payment: ${Downpayment}') try in 3.7 interpreter
# print("(Down payment) :" + Downpayment ) #error try it
print(Downpayment)

