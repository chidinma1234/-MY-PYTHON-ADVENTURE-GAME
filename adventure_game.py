import random
import time

# Choose a random weapon
enemy_list = ['lion', 'tiger', 'cheeta', 'dragon']
enemy = ''

# The initial weapon of the user will be knife
weapon = 'knife'


# Print and pause info passed as msg
def print_pause(msg):
    print(msg)
    time.sleep(3)


# User choice to play the game again
def play_again():
    choice = get_input("Would you like to play again? (yes/no)\n",
                       ['yes', 'no'])
    if choice == 'yes':
        global weapon
        print_pause("Bravo! Starting the game again...")
        weapon = 'knife'
        start_game()
    else:
        finish_game()


# Decision stage
def decide():
    print_pause("Enter 1 to knock on the door of the mansion.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choose_one_or_two()


# Function to make the user choose to
# Advance to mansion or choose a weapon
def choose_one_or_two():
    choice = get_input("Please enter 1 or 2.\n", ['1', '2'])
    if choice == '2':
        advance_to_mansion()
    else:
        change_weapon()


# When the user pick 2
def advance_to_mansion():
    print_pause("You approach the door of the mansion.")
    print_pause("You are about to knock when the door opens and out steps a "
                + enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s mansion!")
    print_pause("The " + enemy + " attacks you!")
    fight_or_run_away()


# Function to fight or run away
def fight_or_run_away():
    choice = get_input("Would you like to (1) fight or (2) run away?\n",
                       ['1', '2'])
    if choice == '1':
        fight()
    else:
        run_away()


# User's choice
def get_input(prompt, values):
    while True:
        choice = input(prompt).lower()
        if choice in values:
            return choice


# Fight the enemy
def fight():
    if weapon == 'gun':
        print_pause("As the " + enemy + " moves to attack, you unsheath" +
                    " your new " + weapon + ".")
        print_pause("The " + weapon + " of Ogoroth shines brightly in your" +
                    " hand as you brace yourself for the attack.")
        print_pause("But the " + enemy + " takes one look at your shiny" +
                    " new toy and runs away!")
        print_pause("You have rid the town of the " + enemy +
                    ". You are victorious!")
    else:
        print_pause("You do your best...")
        print_pause("But your " + weapon + " is no match for the "
                    + enemy + ".")
        print_pause("You have been defeated!")
    play_again()


# Run away from the enemy
def run_away():
    print_pause("You run back into the field. Luckily, you don't seem to" +
                " have been followed.")
    decide()


# change weapon of the user
def change_weapon():
    global weapon
    print_pause("You peer into the cave.")
    if weapon == 'dagger':
        print_pause("You've been here before, and gotten all the" +
                    " good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You discard your silly old " + weapon +
                    " and take the dagger with you.")
        weapon = 'dagger'
    print_pause("You walk back out to the field.")
    decide()


# Finish the game
def finish_game():
    print("Thanks for playing this adventure game! See you next time.")


# Print information about the adventure game
def start_game():
    global enemy
    enemy = random.choice(enemy_list)
    print_pause("You find yourself standing in an open field, filled" +
                " with grass and yellow widlflowers and sunflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere around" +
                " here, and has been terrifying the nerby village.")
    print_pause("In front of you is a mansion.")
    print_pause("To your right is a mysterious dark cave.")
    print_pause("In your hand you held your trusty (but not very effective)"
                + " " + weapon + ".")
    decide()


# Start the adventure game
start_game()

        