import random

# Game Function
def game_win(comp, you):
    # When Both choose same
    if comp == you:
        return None
    # When Computer choose snake
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    # When Computer choose water
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    # When Computer choose gun
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True   


# Computer's Turn                
print("Computer Turn: Snake(s) water(w) or gun(g)?")
rand_no = random.randint(1, 3)

if rand_no == 1:
    comp = 's'
elif rand_no == 2:
    comp = 'w'
elif rand_no == 3:
    comp = 'g'

# Player Turn
you = input("Your Turn : Snake(s) water(w) or gun(g)? ")

print(f"\nComputer chose '{comp}'")
print(f"You chose '{you}'\n")

# Function call
a = game_win(comp,you)
if a == None:
    print("The game is a Tie!")
elif a:
    print("Congratulations! You Win")
else:
    print("You Lose!")        

