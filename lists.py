names = ["John","Kwesi","Ama","Yaw"]
print(names[-1])                    #colon to select a range of items

names = ["John","Kwesi","Ama","Yaw"]
print(names[::2])    

names = ["John","Kwesi","Ama","Yaw"]
names[0] ="Jon"                         #the list can be appended
print(names)    

numbers = [3,4,9,7,1,3,5,]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

print("2 D L I S T S")          #MACHINE LEARNING AND MATRICS(RECTANGULAR ARRAY OF NUMBERS)

#MATRIX = [LIST]

matrix = [                      # EACH ITEM REPRESENTS ANOTHER LIST
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0])

matrix = [                      # EACH ITEM REPRESENTS ANOTHER LIST
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for row in matrix:
    for item in row:
        print(item)

# list methods


# numbers = [3,4,5,9,7,1,3,5,]
# numbers.append(20)                      # TO ADD THE NUMBER TO THE LIST
# numbers.insert(0,8)                     # INSERTED AT THE INDEX YOU DETERMINE
# numbers.remove(1)
# numbers.clear()             #REMOVES EVERYTHING IN THE LIST
# # numbers.pop()               #LAST NUMBER IS REMOVED FROM THE LIST  
# #print(numbers.index(3))                #shows what number is set at that index
# #print(50 in numbers)            # to check if it is present in the list --- generates a boolean
# print(numbers.count(5))
# numbers.sort()   sorts out the list in ascending order
# numbers.reverse() sorts in descending order
# numbers.copy()   to copy the list 

numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)