def check_rounds(question):
    while True:
        response = input(question)

        round_error = "Please enter an integer more than 1 or leave blank for infinite rounds"

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

while True:
    print("how many questions would you like to answer?")
    question_count = check_rounds(">>> ")

    # generate a different heading depending on if user chose infinite rounds or not
    if question_count == "":
        heading = "program continues, Infinite rounds"

    else:
        heading = "program continues"

    print(heading)