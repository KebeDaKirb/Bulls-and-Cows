import random

BANNER = """
oooooooooo.              oooo  oooo                                            .o8         .oooooo.                                       
`888'   `Y8b             `888  `888                                           "888        d8P'  `Y8b                                      
 888     888 oooo  oooo   888   888   .oooo.o       .oooo.   ooo. .oo.    .oooo888       888           .ooooo.  oooo oooo    ooo  .oooo.o 
 888oooo888' `888  `888   888   888  d88(  "8      `P  )88b  `888P"Y88b  d88' `888       888          d88' `88b  `88. `88.  .8'  d88(  "8 
 888    `88b  888   888   888   888  `"Y88b.        .oP"888   888   888  888   888       888          888   888   `88..]88..8'   `"Y88b.  
 888    .88P  888   888   888   888  o.  )88b      d8(  888   888   888  888   888       `88b    ooo  888   888    `888'`888'    o.  )88b 
o888bood8P'   `V88V"V8P' o888o o888o 8""888P'      `Y888""8o o888o o888o `Y8bod88P"       `Y8bood8P'  `Y8bod8P'     `8'  `8'     8""888P' 
"""
ANS_LENGTH = 4
MAX_GUESS = 10
count = 1
seceret = random.sample(range(1, 10), 4)

print(BANNER)


# print(f"Seceret: {seceret}")
def guess_calc(user_guess: str) -> list:
    guess = []
    error_feedback = ""
    try:
        guess = [int(char) for char in list(user_guess)]
        if len(guess) != ANS_LENGTH:
            error_feedback = f"Your answer is longer than {ANS_LENGTH}. Invalid Answer!"
            guess = []
    except ValueError:
        error_feedback = "No non-numbers allowed! Invalid Answer!"
        guess = []
    return guess, error_feedback


while count <= MAX_GUESS:
    guess, error_feedback = guess_calc(user_guess=input(f"Guess {count}:\n"))
    if not guess:
        print(error_feedback)
        continue
    # else:
    #   print(f"Your guess was: {guess}")

    bulls = 0
    cows = 0
    for x in range(ANS_LENGTH):
        if guess[x] == seceret[x]:
            bulls += 1
        elif guess[x] in seceret:
            cows += 1
    print(f"Cows: {cows}\nBulls: {bulls}")
    print("-" * 80)
    count += 1
    if bulls == ANS_LENGTH:
        print("You Win!")
        break
    if count > MAX_GUESS:
        print("You Lost!")
        break
