print('Welcome to Pop Trivia!')

trivia_1 = "Who is Luke Skywalker's father?"
triv_1_ans = "darth vader"
trivia_2 = "What character does Chris Hemsworth play in the Marvel movies?"
triv_2_ans = "thor"
trivia_3 = "What fictional character would you not like when he's angry?"
triv_3_ans = "the hulk"
trivia_4 = "What is a famous style of animation originating from Japan?"
triv_4_ans = "anime"
trivia_5 = "Who was a famous business reality tv star, who had a failed political career?"
triv_5_ans = "trump"

triv_ques = [trivia_1, trivia_2, trivia_3, trivia_4, trivia_5]
triv_ans = [triv_1_ans, triv_2_ans, triv_3_ans, triv_4_ans, triv_5_ans]

correct = []
def pop_trivia():
    count = 0
    guess = input(triv_ques[0 + count] +  "\nEnter response here: ")
    while count < 4:
        if guess.lower() in triv_ans:
            correct.append(triv_ans[0 + count])
            count += 1
            triv_guess = input(triv_ques[0 + count] +  "\nEnter response here: ")
        elif guess.lower() == "quit":
            print("Goodbye!")
            print(correct)
            break
        else:
            count += 1
            guess = input(triv_ques[0 + count] +  "\nEnter response here: ")
    return correct
        
pop_trivia()

right_ans = 0
incorrect = 0
guess_counter = 0

while guess_counter < 4:
    for guess in correct:
        range(len(correct))    
        if guess in triv_ans:
            guess_counter += 1
            right_ans += 1
        else:
            guess_counter += 1
            incorrect += 1

percent =  (right_ans - 3) * 20
print(percent, "%")
