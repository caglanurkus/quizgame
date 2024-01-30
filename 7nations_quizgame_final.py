import time

def ask_question(question, choices, correct_answer, score, time_limit=11, points=1):
    print(question)
    
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    start_time = time.time()
    user_answer = input("Your answer: ")
    end_time = time.time()

    if end_time - start_time > time_limit:
        print("Took too long, sorry.")
    elif user_answer.isdigit() and 1 <= int(user_answer) <= len(choices):
        if choices[int(user_answer)-1][0].lower() == correct_answer.lower():
            print(f'Correct!! You earned {points} point(s)!')
            score += points
        else:
            print('Sorry, wrong answer')
    else:
        print('Invalid choice. Please enter a number corresponding to your choice.')

    print(f"Your current score is: {score}")
    return score

print('Welcome to the 7 Nations of Teyvat Quiz')
score = 0

questions = [
    ('Which nation is famous with poetry? ', ['a. Mondstadt', 'b. Liyue', 'c. Fontaine'], 'a', 1),
    ('Where can sakura blooms be found? ', ['a. Mondstadt', 'b. Inazuma', 'c. Sumeru'], 'b', 1),
    ('Which nation had "yakshas" to protect their region? ', ['a. Mondstadt', 'b. Liyue', 'c. Inazuma'], 'b', 1),
    ('Which nation is known by "wisdom"? ', ['a. Mondstadt', 'b. Liyue', 'c. Sumeru'], 'c', 1),
    ('Which nation is known by their "justice"? ', ['a. Snezhnaya', 'b. Fontaine', 'c. Inazuma'], 'b', 1),
    ('Which nation had Vision Hunt Decree? ', ['a. Mondstadt', 'b. Inazuma', 'c. Liyue'], 'b', 1),
    ('Which nation has Maison Gardiennages as the governing body? ', ['a. Fontaine', 'b. Natlan', 'c. Inazuma'], 'a', 1),
    ('Which nation worships the Cryo Archon? ', ['a. Mondstadt', 'b. Snezhnaya', 'c. Liyue'], 'b', 1),
    ('Which nation worships the God of War? ', ['a. Natlan', 'b. Liyue', 'c. Sumeru'], 'a', 1),
    ('Which nation is known for its intricate contracts and negotiations? ', ['a. Sumeru', 'b. Natlan', 'c. Fontaine'], 'c', 2),
    ('Which nation is home to the Crux Fleet? ', ['a. Mondstadt', 'b. Inazuma', 'c. Liyue'], 'a', 2),
    ('Which nation is ruled by the Electro Archon? ', ['a. Inazuma', 'b. Fontaine', 'c. Natlan'], 'a', 3)
]

for question, choices, answer, points in questions:
    score = ask_question(question, choices, answer, score, time_limit=11, points=points)

print(f"Your final score is: {score}")
