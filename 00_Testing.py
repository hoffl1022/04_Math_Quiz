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


# checks if question amount input is an integer more than 0
def check_rounds(question):
    while True:
        response = input(question)

        round_error = "Please enter a number that is more than 0 or leave blank for infinite rounds"

        # If infinite mode not choose, check response is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# prints instructions
def instructions():
    print("Welcome to my math quiz!\n"
          "\n"
          "first you'll need to choose a difficulty out of the 4 options:\n"
          "Beginner\n"
          "Intermediate\n"
          "Expert\n"
          "(Or you can just type the first letter of the difficulty)\n"
          "\n"
          "Then you'll need to put in how many questions you would like to answer\n"
          "Or you can leave it blank for infinite questions\n"
          "\n"
          "Now you can have some fun answering questions!")
    return ""


# checks if user input is a number
def int_checker(question):
    while True:
        response = input(question)

        if response == "xxx":
            return response

        else:
            try:
                response = int(response)

            except ValueError:
                print("please enter an integer")
                continue

        return response


yes_no_list = ["yes", "no"]
equation_type_list = ["add", "sub", "mul", "div"]
difficulty_list = ["beginner", "intermediate", "expert"]

questions_right = 0
questions_answered = 0

print("Have you played this quiz before?")
played_before = choice_checker(">>> ", yes_no_list, "please choose y / n")

if played_before == "no":
    instructions()

print("\nwhat difficulty would you like?")
difficulty = choice_checker(">>> ", difficulty_list, "please choose B / I / E")

print("\nhow many questions would you like?")
rounds = check_rounds(">>> ")

while True:

    # generate a different heading depending on if user chose infinite rounds or not
    if rounds == "":
        heading = f"\n=== Infinite questions, Question {questions_answered + 1} ==="

    else:
        heading = f"\n=== Question {questions_answered + 1} of {rounds} ==="

    print(heading)

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

    # if user chooses expert difficulty
    else:

        # randomly chooses a question type
        question_type = random.choice(equation_type_list[:-1])

        # generates an addition question
        if question_type == "add":
            num_1 = random.randint(750, 2500)
            num_2 = random.randint(750, 2500)
            answer = num_1 + num_2
            math_question = f"what is {num_1} + {num_2}? "

        # generates a subtraction question
        elif question_type == "sub":
            num_1 = random.randint(750, 2500)
            num_2 = random.randint(750, 2500)
            answer = num_1 - num_2
            math_question = f"what is {num_1} - {num_2}? "

        # generates a multiplication question
        else:
            num_1 = random.randint(25, 250)
            num_2 = random.randint(10, 50)
            answer = num_1 * num_2
            math_question = f"what is {num_1} x {num_2}? "

    print(f"\n{math_question}")
    user_answer = int_checker(">>> ")

    if user_answer == "xxx":
        break
    elif user_answer == answer:
        print("-----------------------\n"
              "✅ you got it right! ✅\n"
              "-----------------------")
        questions_right += 1
    else:
        print("----------------------\n"
              "❌ you got it wrong ❌\n"
              "----------------------")

    questions_answered += 1

    if rounds == questions_answered:
        break

print(f"\nYour score was {questions_right}/{questions_answered}")
