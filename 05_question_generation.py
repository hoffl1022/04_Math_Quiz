import random
question_type = ""
sign = ""
while True:

    question_type = input("what question type? ")

    # number 1 and 2 will be used for addition and subtraction
    num_1 = random.randint(50, 200)
    num_2 = random.randint(50, 200)

    # number 3 and 4 will be used for division and multiplication
    num_3 = random.randint(10, 40)
    num_4 = random.randint(2, 15)

    # generates a question based on the equation type
    if question_type == "add":
        answer = num_1 + num_2
        question = f"what is {num_1} + {num_2}"

    elif question_type == "sub":
        answer = num_1 - num_2
        question = f"what is {num_1} - {num_2}"

    elif question_type == "mul":
        answer = num_3 * num_4
        question = f"what is {num_3} x {num_4}"

    else:
        answer = num_3 / num_4
        question = f"what is {num_3} ÷ {num_4}"

    print(question)
    print(f"the answer is: {answer}\n")

