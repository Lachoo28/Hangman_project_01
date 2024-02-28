from settings import Settings
from random import choice
from art import tprint
from time import sleep
from os import system, name

class Hangman:
    def __init__(self):
        self.clear_screen()
        self.settings = Settings()
        self.words_easy = self.settings.words["easy"]
        self.words_medium = self.settings.words["medium"]
        self.words_hard = self.settings.words["hard"]
        self.start()

    @staticmethod
    def clear_screen():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def start(self):
        tprint("Welcome to Hangman Game")
        while True:
            choice = self.get_choice("1. Play\n2. Settings\n3. Exit\nSelect an Option (1/2/3): ", [1, 2, 3])
            if choice == 1:
                self.clear_screen()
                self.play()
            elif choice == 2:
                self.clear_screen()
                self.edit_settings()
            else:
                print("Thank you for playing Hangman Game")
                sleep(1)
                exit()

    def edit_settings(self):
        print("------- Settings -------")
        print(f"1. Number of Chances: {self.settings.turns}")
        print(f"2. Difficulty Level: {self.settings.level}")
        print("3. Add a Word to Dictionary")
        print("4. Remove a Word from Dictionary")
        print("5. View Score")
        print("6. Reset Score")
        print("7. Back to Main Menu")

        while True:
            settings_option = self.get_choice("Select an Option (1/2/3/4/5/6/7): ", [1, 2, 3, 4, 5, 6, 7])
            self.clear_screen()
            if settings_option == 1:
                self.settings.change_turns()
            elif settings_option == 2:
                self.settings.change_level()
            elif settings_option == 3:
                self.settings.add_word()
            elif settings_option == 4:
                self.settings.remove_word()
            elif settings_option == 5:
                self.settings.view_score()
            elif settings_option == 6:
                self.settings.reset_score()
            else:
                self.start()

    def play(self):
        word_list = self.words_easy if self.settings.level == 1 else self.words_medium if self.settings.level == 2 else self.words_hard
        word = choice(word_list)
        characters = ["_"] * len(word)
        temp_word = word
        turns = self.settings.turns

        while turns > 0 and "_" in characters:
            print(" ".join(characters))
            guess = input("Guess a letter: ")

            if len(guess) == 1:
                if guess in word:
                    for index, letter in enumerate(word):
                        if letter == guess:
                            characters[index] = guess
                    print("Correct!")
                else:
                    turns -= 1
                    print(f"Incorrect! Turns left: {turns}")
            else:
                print("Please enter only one letter.")

        if "_" not in characters:
            print(f"\nCongratulations! You won!\nThe correct word is {''.join(characters)}")
            self.settings.set_score("win")
        else:
            print(f"\nSorry! You lost!\nThe correct word is {temp_word}")
            self.settings.set_score("lost")

        self.play_again()

    def play_again(self):
        replay = input("\nPress any key to play again or (f) to go to Main Menu: ")
        if replay.lower() == "f":
            self.start()
        else:
            self.clear_screen()
            self.play()

    @staticmethod
    def get_choice(prompt, options):
        while True:
            try:
                choice = int(input(prompt))
                if choice in options:
                    return choice
                else:
                    raise ValueError
            except ValueError:
                print("Please select a valid option.")

Hangman()
