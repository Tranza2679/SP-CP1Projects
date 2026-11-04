attempts = 0
def increase():
    return attempts + 1
def stupid_proof(user_answer, correct):
    """"This stupid proofs stuff, this a comment for a fuction!"""
    user_answer = user_answer.strip().title()
    if user_answer in correct:
        return True, user_answer, increase()
    else:
        return False, user_answer, increase()
while True:
    capital = input("What is the capital of Utah ")
    correct, capital, attempts = stupid_proof(capital,  ["Salt Lake City", "Slc", "Salt Lake"])
    if correct:
        print(f"Good job {capital} is the capital of Utah")
        break
    else:
        print(f"Try again. {capital} is not the capital of Utah. You have tried {attempts} times")
