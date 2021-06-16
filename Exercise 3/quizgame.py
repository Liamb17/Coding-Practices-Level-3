'''
    File name: quizgame.py
    Author: Liam Bishop
    Date created: 12/06/2021
    Date last modified: 12/06/2021
    Version: 0.0.1
    Copyright: © Liam Bishop.
    Python Version: 3.7.9
    Concept: The game is simple, you will be presented with a series of multi choice questions with
    3 answers, the player must enter the letter of the answer they believe to be correct, If you win
    the game, your printer will sprint out a slice of toast - compatible printer required
    Rules: 1) player must answer the questions 2) Player must hold their hand in the air while answering 3) They must stand on 1 leg while thinking of the answer.
'''
import random
import json
def loadquestions() :
    
    try:
        with open('quizquestions.json') as json_file:
            questions = json.load(json_file)
            
            # Unable to load questions, display error
            if type(questions) != dict :
                print("Unable to load questions file - is it the correct format?")
                exit()
                
            return questions

    except (FileNotFoundError):
        # Error, File doesn't exist
        print("Unable to load questions file - does the file exist?")
        exit()
    except ValueError:
        # Error loading json
        print("Unable to load questions file")
        exit()
    
def ask_rules_verification() :
    print("The game is simple, you will be presented with a series of multi choice questions with 3 answers")
    print("You must enter the letter of the answer you believe to be correct")
    print("If you win the game, your printer will sprint out a slice of toast*")
    print("* compatible printer required")
    print("** Rules **")
    print("1) You must answer the questions")
    print("2) Hold your hand in the air while answering")
    print("3) You must stand on 1 leg while thinking of the answer")
    
    while True :
        # Ask user if they are happy to follow the rules
        confirm = input("Are you happy to play the game with those rules? [yes/no]").lower()

        if confirm == "yes" :
            return True
        elif confirm == "no" :
            return False
        else :
            # Invalid Response, Retry
            print("Please enter a response of yes or no")

def ask_game_length() :    
    while True :
        # Ask user how many rounds they would like to play
        number = input("How many rounds would you like to play? [3 or 5]")

        if number == "3" or number == "5" :
            return number
        elif (type(number) == int or float) :
            print("Please enter a value of 3 or 5 rounds")
        else :
            # Invalid Response, Retry
            print("Please enter a numeric response")

# Try load questions for the game
questions = loadquestions()

# Define variables needed for this game
score = 0

# Collect players name
playername = input("Enter your player name: ")

# Welcome the player to the game!
print("Welcome to the world of random questions, "+playername+"!!")

# Display the rules verification question
result = ask_rules_verification()
# Check if user didn't accept the rules
if result is False:
    # User rejected the rules, close the game down
    print("Sad to see you go "+playername+". We hope to see you next time!")
    exit()
    
# User has confirmed rules, we can now start the game
# We don't ask the user to reconfirm the rules if they are replaying as they've already confirmed these
while True:
    
    # Ask user how many rounds they'd like to play
    game_length = ask_game_length()
    # Randomise the list of questions so its different everytime
    random.shuffle(questions["questions"])
    # Loop through the questions
    print(game_length);
    for question in questions["questions"][:int(game_length)]:
        answer_keys = []
        
        # Display the question to the player
        print(question["question"])
        # Output the answers and loop through the answers
        print("Answers")
        for answer in question["answers"]:
            # Output answer
            print(answer["id"]+") "+answer["value"])
            # Add answer ID to the list
            answer_keys.append(answer["id"].upper())
           
        while True :
            # Ask the player to enter there answer
            answer_keys_concentrated = ', '.join(answer_keys)
            entered_answer = input("Please enter your answer: ["+answer_keys_concentrated+"]").upper()
            
            # Check if the player entered the correct answer
            if entered_answer == question["correct_answer"].upper() :
                print("Congrats "+playername+". You got 10 points!!")
                score += 10
                break
            elif entered_answer in answer_keys:
                print("Aww, what a shame. That wasn’t the correct answer. You got 0 points")
                break
            else :
                # Invalid answer entered
                print("Invalid answer, please enter one of the following answers: "+answer_keys_concentrated)
                
    # Determine the required score for the game length
    if game_length == "3":
        required_score = 20
    elif game_length == "5":
        required_score = 40
    else :
        # This statement shouldn't be reachable, but default to a score of 20 just incase to avoid errors
        required_score = 40
        
    # Check if the accumilated score is higher or equal to the required score
    if (score >= required_score):
        print("Bravo, bravo "+playername+"! You’ve won the round!")
    else:
        print("Oh dear. So close and yet so far. Good luck next time "+playername+"!")

    # Well that was fun, lets see if the player would like to play again!
    replay = input("Would you like to play again? [yes/no] ");
    if replay == "yes":
        continue;
    
    elif replay == "no":
        # User has had enough, Lets thank them and finish the game
        print("Thank you for playing "+playername+". See you next time!")
        break

    else:
        # Invalid Response, Retry
        print("Please enter a response of yes or no")