import random

num_1 = round(random.uniform(100, 500), 2)
num_2 = round(random.uniform(20, 75), 2)
answer = num_1 + num_2
math_question = f"what is {num_1} + {num_2}? "

print(math_question)
print(f"the answer is {answer:.2f}")
