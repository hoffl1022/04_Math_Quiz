# Check users response is valid
def choice_checker(question, valid_list, error):
    while True:
        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item),
        # the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)


yes_no_list = ["yes", "no"]
equation_list = ["multiplication", "addition", "subtraction", "division"]
while True:
    played_before = choice_checker("have you played this game before?", yes_no_list, "please answer y / n")

    if played_before == "no":
        print("Instructions go here")
    else:
        print("program continues")

    question_type = choice_checker("what kind of questions do you want? ", equation_list, "please choose a / s / m / d")
    