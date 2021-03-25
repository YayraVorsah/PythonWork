numbers = (1,2,3,3)         # Tuples use this bracket and cannot be modified or changed
print(numbers[0])


print("U N P A C K I N G")

coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x,y,z = coordinates   # this is the same as the above statment   CAN BE USED ON LISTS TOO



# print("DICTIONARIES DICTIONARY")
# Name : John Smith
# Email: john@gmail.com
# Phone: 1234                 # THE KEYS HERE ARE THE NAME, email, Phone, 

customer = {
    "name": "John smith ",
    "age": 30,                                              #EACH KEY SHOULD BE UNIQUE AND NOT DUPLICATED
    "is_verified": True
}                                                            #USES THE CURLY BRACKETS
#the value can be anything
#print(customer["name"])             # if you specify a key that does not exist IT GIVES AN ERROR
print(customer.get("birthdate"))             # THIS WOULD RETURN ''NONE'' IF IT IS NOT PRESENT -------no box bracket here#

# NONE --- represents the absence of a value

print(customer.get("birthdate", "Jan 1 1980"))      #INTRODUCTION OF DEFAULT VALUES (----would print the date )

#APPENDING THE DICTIONARY
#customer["name":"Jack smith"]
#ADDING NEW KEY VALUE PAIRS

#customer["birthdate":"1st January"]


phone = input("Phone:")
digits_mapping = {
    "1": "One",
    "2": "two",
    "3": "Three",
    "4": "Four",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

# EMOJIS CONVERTER

message = input(">")
words = message.split(" ")
emojis = {
    ":)": "HAPPY EMOJI ",
    ":(": " SAD EMOJI",
    ";)": "SMILE"
}

for word in words:
    output += emojis.get(word, word)
print(output)








