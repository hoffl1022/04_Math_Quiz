import random
sign = ""
equation_type_list = ["add", "sub", "mul", "div"]

difficulty = input("what difficulty do you want? ")

while True:

    if difficulty == "b":
        num_1 = random.randint(15, 30)
        num_2 = random.randint(15, 30)
        answer = num_1 + num_2
        question = f"what is {num_1} + {num_2}?"

    elif difficulty == "i":

        # randomly chooses either addition or subtraction
        question_type = random.choice(equation_type_list[:-2])

        # generates an addition question
        if question_type == "add":
            num_1 = random.randint(50, 300)
            num_2 = random.randint(50, 300)
            answer = num_1 + num_2
            question = f"what is {num_1} + {num_2}?"

        # generates a subtraction question
        else:
            num_1 = random.randint(50, 300)
            num_2 = random.randint(50, 300)
            answer = num_1 - num_2
            question = f"what is {num_1} - {num_2}"

    elif difficulty == "h":

        # randomly chooses a question type
        question_type = random.choice(equation_type_list[:-1])

        if question_type == "add":
            num_1 = random.randint(750, 2500)
            num_2 = random.randint(750, 2500)
            answer = num_1 + num_2
            question = f"what is {num_1} + {num_2}?"

        elif question_type == "sub":
            num_1 = random.randint(750, 2500)
            num_2 = random.randint(750, 2500)
            answer = num_1 - num_2
            question = f"what is {num_1} - {num_2}?"

        else:
            num_1 = random.randint(25, 250)
            num_2 = random.randint(10, 50)
            answer = num_1 * num_2
            question = f"what is {num_1} x {num_2}?"

    else:

        # randomly chooses a question type
        question_type = random.choice(equation_type_list)

        if question_type == "add":
            num_1 = random.randint(2000, 5000)
            num_2 = random.randint(2000, 5000)
            answer = num_1 + num_2
            question = f"what is {num_1} + {num_2}?"

        elif question_type == "sub":
            num_1 = random.randint(2000, 5000)
            num_2 = random.randint(2000, 5000)
            answer = num_1 - num_2
            question = f"what is {num_1} - {num_2}?"

        elif question_type == "mul":
            num_1 = random.randint(100, 500)
            num_2 = random.randint(20, 75)
            answer = num_1 * num_2
            question = f"what is {num_1} x {num_2}?"

        else:
            num_1 = random.randint(100, 500)
            num_2 = random.randint(10, 50)
            answer = num_1 / num_2
            question = f"what is {num_1} ÷ {num_2}?"

    print(f"\n{question}")
    print(f"the answer is {answer}")
    input("====")
