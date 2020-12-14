import random as rd

a = rd.randint(999,9999)
b = str(a)
c = list(b)
print(c)

inp = list(input("Enter your guess"))

"""def game():
        bull = 0
        cow = 0
        for iter in c:
            if inp1.index(iter) == c.index(iter):
                bull = bull + 1
                if bull == 4:
                    print("You got em")
                    break
                else:
                    game()
            else:
                cow = cow + 1
                game()
"""


def get_response(ans, correct_ans):
    print("Your ans " )
    print(ans)
    print("Correct ans ")
    print(correct_ans)
    bulls = 0
    cows = 0

    for i in range(len(ans)):
        for j in range(len(correct_ans)):
            if ans[i] == correct_ans[j]:
                if i == j:
                    bulls = bulls + 1
                else:
                    cows = cows + 1

    return [bulls, cows]








try:
    x = 0
    y = get_response(inp, c)#game(x)
    print(y)
    """
        if game(x) == 4:
        print("You got em")
    else:
        game(x)
        print(y)
        
    """

except:
    print("You have failed")




