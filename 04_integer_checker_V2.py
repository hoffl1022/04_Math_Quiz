# Version 2 gives the option for negative numbers to be allowed or not

def int_check(question, negative):
    while True:
        response = input(question).lower()

        round_error = "Please type an integer that is more than 0"

        # Check if integer is more than zero
        if negative == "n":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue
        else:
            try:
                response = int(response)

            except ValueError:
                print(round_error)
                continue
        return response


while True:
    question_count = int_check("how many questions do you want to answer? ", "y")
    print(question_count)
