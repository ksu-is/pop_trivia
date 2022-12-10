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
triv_5_ans = "donald trump"

triv_ques = [trivia_1, trivia_2, trivia_3, trivia_4, trivia_5]
triv_ans = [triv_1_ans, triv_2_ans, triv_3_ans, triv_4_ans, triv_5_ans]

correct = []
def pop_trivia():
    counter = 5
    guess = input(triv_ques[4 - counter] +  "\nEnter response here: ")
    while counter != 0:
            if guess.lower() in triv_ans:
                if guess.lower() == triv_ans[4 - counter]:
                    correct.append(triv_ans[4 - counter])
                    counter -= 1
                    guess = input(triv_ques[4 - counter] +  "\nEnter response here: ")
            else:
                break
    return correct
        
pop_trivia()

right_ans = 0
incorrect = 0
guess_counter = 0

while guess_counter < 5:
    for guess in correct:
        range(len(correct))    
        if guess in triv_ans:
            guess_counter += 1
            right_ans += 1
        else:
            guess_counter += 1
            incorrect += 1

percent = right_ans * 20
print("Your score is:", percent, "%")
