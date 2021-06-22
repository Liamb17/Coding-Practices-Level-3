'''
    File name: paragraph_generator.py
    Author: Liam Bishop
    Date created: 22/06/2021
    Date last modified: 22/06/2021
    Version: 0.0.1
    Copyright: © Liam Bishop.
    Python Version: 3.7.9
    Description: The script will create a file containing the paragraphs, once launched it will ask the user which paragraph to display before ending
'''
# Define imports
import datetime

# Define Paragraph
class Paragraph:
    def __init__(self):
        # Create the file containing the paragraphs
        f = open("notebook-paragraphs.txt", "w")
        f.write("What if I said that randomness, coincidence, chance, karma, miracle—all such notions do not exist? That from the moment a being is born, their future is already carved into stone?\n")
        f.write("If so, a being’s actions do not truly stem from his own choices, but are manipulated to suit the performance of a “conductor”. In that sense—prayer, perfection and imperfection, reality and dream, hope and despair, righteousness and wickedness, love and hatred and even life and death are but illusionary concepts—equally and utterly devoid of meaning.\n")
        f.close()

    def display_paragraph(self, choice):
        # Define current date
        date = datetime.datetime.now()
        # Load the file containing paragraphs
        f = open("notebook-paragraphs.txt", "r")
        # Print paragraph choosen and copyright, deduct 1 from the choosen choice due to python starting from 0 not 1
        print(f.readlines()[(choice-1)])
        print("© Todoki "+date.strftime("%Y"))

    def ask_paragraph(self) :    
        while True :
            # Ask user how many rounds they would like to play
            print("Which paragraph would you like to display?")
            print("Please enter a numeric value of the paragraph you'd like to display")
            print("1 = 1st paragraph")
            print("2 = 2nd paragraph")
            number = input("Please enter your answer 1 or 2? [1 or 2]")

            if number == "1" or number == "2" :
                return int(number)
            elif (type(number) == "int" or "float") :
                print("Please enter a value of 1 or 2")
            else :
                # Invalid Response, Retry
                print("Please enter a numeric response")

# Start the paragraph class
p = Paragraph()

# Ask user which paragraph to display
choice = p.ask_paragraph()

# Display paragraph with choice
p.display_paragraph(choice)