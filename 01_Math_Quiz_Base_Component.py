import random


# Functions go here

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


# checks if input is an integer
def num_check(question, allow_negative):
    while True:
        response = input(question).lower()

        if response != "":

            # Check if integer is more than zero
            if allow_negative == "n":
                round_error = "Please type an integer that is more than 0"
                try:
                    response = float(response)

                    if response < 1:
                        print(round_error)
                        continue

                except ValueError:
                    print(round_error)
                    continue
            else:
                round_error = "Please enter a number"
                try:
                    response = int(response)

                except ValueError:
                    print(round_error)
                    continue
        return response


def instructions():
    print("Welcome to my math quiz!\n"
          "\n"
          "first you'll need to choose a difficulty out of the 4 options:\n"
          "Beginner\n"
          "Intermediate\n"
          "Hard\n"
          "Expert\n"
          "(Or you can just type the first letter of the difficulty)\n"
          "\n"
          "Then you'll need to put in how many questions you would like to answer\n"
          "Or you can leave it blank for infinite questions\n"
          "\n"
          "Now you can have some fun answering questions!")
    return ""


yes_no_list = ["yes", "no"]
equation_type_list = ["add", "sub", "mul", "div"]
difficulty_list = ["beginner", "intermediate", "hard", "expert"]

questions_right = 0
questions_wrong = 0
questions_answered = 0

print("Have you played this quiz before?")
played_before = choice_checker(">>> ", yes_no_list, "please choose y / n")

if played_before == "no":
    instructions()

print("\nwhat difficulty would you like?")
difficulty = choice_checker(">>> ", difficulty_list, "please choose B / I / H / E")

print("\nhow many questions would you like?")
rounds = num_check(">>> ", "n")

while True:
    # if user chooses beginner difficulty
    if difficulty == "beginner":
        num_1 = random.randint(10, 40)
        num_2 = random.randint(10, 40)
        answer = num_1 + num_2
        math_question = f"what is {num_1} + {num_2}? "

    # if user chooses intermediate difficulty
    elif difficulty == "intermediate":

        # randomly chooses either addition or subtraction
        question_type = random.choice(equation_type_list[:-2])

        # generates an addition question
        if question_type == "add":
            num_1 = random.randint(50, 300)
            num_2 = random.randint(50, 300)
            answer = num_1 + num_2
            math_question = f"what is {num_1} + {num_2}? "

        # generates a subtraction question
        else:
            num_1 = random.randint(50, 300)
            num_2 = random.randint(50, 300)
            answer = num_1 - num_2
            math_question = f"what is {num_1} - {num_2}? "

    # if user chooses hard difficulty
    elif difficulty == "hard":

        # randomly chooses a question type
        question_type = random.choice(equation_type_list[:-1])

        if question_type == "add":
            num_1 = round(random.uniform(750, 2500), 2)
            num_2 = round(random.uniform(750, 2500), 2)
            answer = num_1 + num_2
            math_question = f"what is {num_1} + {num_2}? "

        elif question_type == "sub":
            num_1 = round(random.uniform(750, 2500), 2)
            num_2 = round(random.uniform(750, 2500), 2)
            answer = num_1 - num_2
            math_question = f"what is {num_1} - {num_2}? "

        else:
            num_1 = random.randint(25, 250)
            num_2 = random.randint(10, 50)
            answer = num_1 * num_2
            math_question = f"what is {num_1} x {num_2}? "

    # if user chooses expert difficulty
    else:

        # randomly chooses a question type
        question_type = random.choice(equation_type_list)

        if question_type == "add":
            num_1 = round(random.uniform(2000, 5000), 4)
            num_2 = round(random.uniform(2000, 5000), 4)
            answer = num_1 + num_2
            math_question = f"what is {num_1} + {num_2}? "

        elif question_type == "sub":
            num_1 = round(random.uniform(2000, 5000), 4)
            num_2 = round(random.uniform(2000, 5000), 4)
            answer = num_1 - num_2
            math_question = f"what is {num_1} - {num_2}? "

        elif question_type == "mul":
            num_1 = round(random.uniform(100, 500), 2)
            num_2 = round(random.uniform(20, 75), 2)
            answer = num_1 * num_2
            math_question = f"what is {num_1} x {num_2}? "

        else:
            num_1 = random.randint(100, 500)
            num_2 = random.randint(10, 50)
            answer = num_1 / num_2
            math_question = f"what is {num_1} ÷ {num_2}? "

    print(f"\n{math_question}")

    # FOR TESTING ONLY, REMOVE AFTER
    print(f"[FOR TESTING] the answer is {answer}")

    user_answer = num_check(">>> ", "y")

    if user_answer == "xxx":
        break

    if user_answer == answer:
        print("-----------------------\n"
              "✅ you got it right! ✅\n"
              "-----------------------")
        questions_right += 1

    else:
        print("----------------------\n"
              "❌ you got it wrong ❌\n"
              "----------------------")
        questions_wrong += 1

    questions_answered += 1

    if rounds == questions_answered:
        break

print(f"\nYour score was {questions_right}/{questions_answered}")
