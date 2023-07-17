def int_check(question):
    while True:
        response = input(question).lower()

        round_error = "Please type either <enter> or an that is more than 0"

        # Check if integer is more than zero
        try:
            response = int(response)

            if response < 1:
                print(round_error)
                continue

        except ValueError:
            print(round_error)
            continue

        return response


while True:
    question_count = int_check("how many questions do you want to answer? ")

