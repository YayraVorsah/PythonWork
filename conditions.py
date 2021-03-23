#Define variable
is_hot = False
is_cold = True
if is_hot:                                  #if true for the first statement then print 
    print("It's a hot day")
    print("drink plenty of water")
elif is_cold:                               # if the above is false and this is true then print this
    print("It's a cold day")
    print("Wear warm clothes")
else:                                       # else you print this if both statements are false
    print("It's a good day")
print("Enjoy your day")

print("EXERCISE")

house_price = 1000000
good_credit = True
bad_credit = False

if good_credit:
    downpay = house_price//10
    print("your downpayment : $" + str(downpay))
else :
    downpay = house_price//20
    print("Your downpay is bad ")
# if good_credit:
#     print("Your down payment is " + good_credit)

print("LOGICAL OPERATORS")
hasHighIncome = True
hasGoodCredit = True

if hasHighIncome and hasGoodCredit:             #Both Conditions need to be true to execute
    print("Eligible for Loan")                     #even if one statement is false(It all becomes false due to the AND operator)
else:
    print("Not eligible for Loan")

hasHighIncome = True
hasGoodCredit = False

if hasHighIncome or hasGoodCredit:             #At least One condition needs to be true to execute 
    print("Eligible for Loan and other goods")                     #even if one statement is false it will execute because of the OR operator)
else:
    print("Not eligible for Loan")

print("NOT OPERATOR")
#has good credit and not a criminal record
good_credit = True
criminalRecord = False       # the not operator would turn this to True

if good_credit and not criminalRecord:          # and not (criminalRecord = False)  === True
    print("you are good to go")
