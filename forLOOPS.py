prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
    print(total)
print(f'Total : {total}')

print("NESTED LOOPSS")

for x in range(4):
  #  print(x)                           # x would print out [0,1,2,3]
    for y in range(3):      # the x would be [0] and y would hold [0,1,2,] againt the x so == [0,1], [0,1], [0,2] before it moves to the second item in x
        print(f'({x}, {y})')

print("C H A L L E N G E")
items = "x"
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    for item in items:
        solution = item * number
        print(solution)



numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += "x"                               #thought this would produce 5 + x, 2 +x, etc
    print(output)




numbers = [2,2,2,2,5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += "x"
    print(output)