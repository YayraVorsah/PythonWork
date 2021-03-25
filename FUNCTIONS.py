def greet_user():               # IN THE PARANTHESIS YOU CAN ADD A PARAMETER TO USE IN YOUR FUNCTION(name)  where name = "John"
    print('Hi there!')
    print('Welcome Aboard')

# 2 LINE BREAKS IMPORTANT AFTER CREATING A FUNCTION


print('Start')
greet_user()                DEFINE THE FUNCTION FIRST B4 YOU CALL IT
print("Finish")

# the parameters receive information for the function
#when a function has a parameter it has to be supplied with an argument

def greet_user(first_name,last_name):               
    print('Hi there!')
    print('Welcome Aboard')

greet_user("John","Ama")        # John & Ama are the arguments (positional arguments)(can be a keyword argument such as ===  first_name="John")
calc_cost(50,10,0.1)
keyword arg should come b4 positional arg


RETURN VALUES
RETURNING RESULTS

def square(number):
    return number * number          # USING PRINT YOU GET(9 AND NONE)

result = square(3)          # BY DEFAULT ALL FUNCTIONS RETURN (---NONE---)


GENERAL RULE
1, THE FUNCTION SHOULD NOT BE CONCERNED WITH RECEIVING AN INPUT
2, IT SHOULD NOT PRINT THE OUTPUT BECUSE IT MIGHT BE USED IN A DIFFERENT WAY

EXAMPLE OF OUR EMOJI EXAMPLE IN TUPLES.PY

def emoji_converter(message):
        
    words = message.split(" ")
    emojis = {
        ":)": "HAPPY EMOJI ",
        ":(": " SAD EMOJI",
        ";)": "SMILE"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter)