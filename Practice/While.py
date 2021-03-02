'''i=1
while i <= 5:
    print(i)
    i+=1;
print("Done")

i=1
while i <= 5:
    print('*' * i)
    i+=1;
print("Done")'''

secret_number=9
Guess=0
Limit=3
while Guess < Limit:
    guess=int(input('Guess: '))
    Guess+=1
    if guess == secret_number:
        print("You Won")
        break #terminates the loop9
else:
    print("You failed")



