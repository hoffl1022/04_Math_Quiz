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


difficulty_list = ["beginner", "intermediate", "hard", "expert"]
while True:

    quiz_difficulty = choice_checker("what difficulty do you want the quiz to be? ", difficulty_list, "please choose either b / i / h / e ")
    print(f"you have chosen {quiz_difficulty} difficulty")
