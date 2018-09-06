from datetime import datetime

name = input("greetings, what is your name?: ")
age = input("what is your age?: ")
print("-----------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------")


print(name + " knows how to party. Age: " + age)

def recursion(repeats, text):
    num = int(repeats)
    while num <= int(repeats) and num >= 0:
        print("#" + str(num) + ": " + text)
        num = num - 1

def repeatChoice():
            repeat = input("Would you like to go again?(y): ")
            if repeat == "y" or repeat == "yes" or repeat == "":
                QA()
            else:
                return

def QA():
    question = input("Ask a question: ")
    if question == "spork" or question == "sporks":
        print("HEY YOU LEAVE SPORKS OUT OF THIS!")
    elif question == "game":
        print("Well I may make a simple text adventure to learn python.. we'll see.")
    elif question == "conditions":
        print("equals: a == b")
        print("not equals: a != b")
        print("less than: a < b")
        print("Greater than: a > b")
        print("Greater than or equal: a >= b")
        print("if, elif, else, and")
        print("and: if a > b and b > c")
    elif question == "exit":
        return
    elif question == "recursion":
        count = input("How many times: ")
        text = input("What to say: ")
        recursion(count, text)
    elif question == "time" or question == "date":
        print(datetime.now())
        repeatChoice()
    elif question == "do math" or question == "math":
        print("Please only use numbers when asked.")
        expression1 = input("first number: ")
        expression2 = input("operator: ")
        expression3 = input("second number: ")
        if expression2 == "x" or expression2 == "*":
            print(int(expression1) * int(expression3))
            repeatChoice()
        if expression2 == "+":
            print(int(expression1) + int(expression3))
            repeatChoice()
        elif expression2 == "/":
            print(int(expression1) / int(expression3))
            repeatChoice()
        elif expression2 == "-":
            print(int(expression1) - int(expression3))
            repeatChoice()
        else:
            print("I'm sorry, I don't know that operator yet...")
            repeatChoice()
    else:
        print('You asked "' + question + '..." Why?')
        repeatChoice()
QA()
