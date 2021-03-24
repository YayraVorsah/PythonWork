print('while condition:')      #as long as the condition is true it would be repetitive   #used to execute a block of code multiple times

y = 1                   #define a variable
while y <= 5:
    print(y)
    y += 1
print("Done")


y = 1                   #define a variable ALWAYS
while y <= 5:
    print('*' * y)
    y += 1


print("GAME PYTHON")

# secretnumber = 9
# guesscount = 0                           #use descriptive names to understand your code
# guesslimit = 3
# while guesscount < guesslimit:
#     guess = int(input("Guess :"))
#     guesscount += 1
#     if guess == secretnumber:
#         print("Yaayy!! You Won!")
#         break                           # if this is achieved the code does not run again
# else:
#     print("Sorry, You failed")


print("CAR GAME --000---000")

command = ""
started = False
while True:
    command = input("> :").lower()
    if command == 'start':
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == 'stop':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped...")
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
""")
    elif command == 'quit':
        break
    else:
        print("Sorry i don't understand that")