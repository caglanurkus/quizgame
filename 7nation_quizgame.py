# %%
print('Welcome to the 7 Nations of Teyvat Quiz')

# %%
score = 0
score = int(score)

# %%
answer1 = await input('Which nation is famous with poetry?')

# %%
if answer1 == 'mondstadt' :
    print('Correct!!')
    score = score + 1
else:
    print('sorry, wrong asnwer')
print("your current score is: " + str(score)) 

# %%
answer2 = await input('Where can sakure blooms be found?')

# %%
if answer2 == 'inazuma' :
    print('correct!!')
    score = score + 1
else:
    print('sorry, wrong answer')
print("your current score is: " + str(score))

# %%
answer3 = await input('Which nation had "yakshas" to protect their region?')


# %%
if answer3 == 'liyue' :
    print('correct!!')
    score = score + 1
else:
    print('sorry, wrong answer')
print("your current score is: " + str(score))  

# %%
answer4 = await input('Which nation knows by "wisdom"?')


# %%
if answer4 == 'sumeru' :
    print('correct!!')
    score = score + 1
else:
    print('sorry, wrong answer')
print("your current score is: " + str(score))

# %%
answer5 = await input('Which nation knows by their "justice"?')


# %%
if answer5 == 'fontaine' :
    print('correct!!')
    score = score + 1
else:
    print('sorry, wrong answer')
print("your current score is: " +str(score))

# %%
print("your final score is: " +str(score))
 

# %%



