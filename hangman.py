import random

trys = 5
score = 0
words = ["death", "music"]
zu_erraten = random.choice(words)
var = zu_erraten.replace(zu_erraten, "-" * len(zu_erraten))


def user_eingabe():
    global user_input
    print(var)
    user_input = str(input("give me an letter\n"))
    eingabe_length = len(user_input)
    user_input = user_input.lower()  # macht den string in kleine buchstaben, groß und klein schreibung somit egal
    if eingabe_length == 1:
        pass
    else:
        print("error")
        user_eingabe()


def decision():
    global score
    global var
    if user_input in zu_erraten:
        stelle = zu_erraten.index(user_input)
        var = var[:int(stelle)] + user_input + var[int(stelle + 1):]
    else:
        pass
    if var == zu_erraten:
        print("win")
        exit()
    elif user_input in zu_erraten:
        print("correct")
    else:
        print("false")
        score = score + 1
        print(f"score: {score}")


while score < trys:
    user_eingabe()
    decision()

if score == trys:
    print("lose")
