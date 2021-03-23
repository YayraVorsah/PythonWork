# used to compare a variable and a value

temperature = 30
if temperature != 30:
    print("It's a hot day today")
else:
    print("It's a good day today")

print("EXERCISE")

nameOfP = "Yayra"
if len(nameOfP) < 3:
    print("Name must be more than 3 characters")
elif len(nameOfP) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name is good")


print("WEIGHT CONVERTER COURSE")

collect = int(input("Weight :"))                    # NOTE THAT the results of an inpput is a STRING
collectType = input("(L)bs or (K)G :")
if collectType.upper == "L":
    calc = collect * 0.45
    print(f"You are {calc} kilos")
else:
    calc = collect // 0.45
    print(f"You are {calc} pounds")



