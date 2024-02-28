import json
from time import sleep

def read_file():
    with open("settings.json", "r") as f:
        return json.load(f)

def save_file(dictionary):
    with open("settings.json", "w") as f:
        json.dump(dictionary, f, indent=4)

class Settings:
    def __init__(self):
        settings = read_file()
        self.turns = settings["turns"]
        self.level = settings["level"]
        self.words = settings["words"]
        self.score = settings["score"]

    def change_turns(self):
        chances = None
        while not chances:
            try:
                chances = int(input("Enter the number of chances you want: "))
                if chances < 1:
                    chances = None
                    raise ValueError()
            except ValueError:
                print("Please enter a number greater than 0")
        settings = read_file()
        settings["turns"] = chances
        save_file(settings)
        self.turns = chances

    def change_level(self):
        print("Select the difficulty level")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        difficulty = None
        while not difficulty:
            try:
                difficulty = int(input("Select from 1/2/3: "))
                if difficulty not in [1, 2, 3]:
                    difficulty = None
                    raise ValueError()
            except ValueError:
                pass

        settings = read_file()
        settings["level"] = difficulty
        save_file(settings)
        self.level = difficulty

    def add_word(self):
        new_word = input("Enter the word: ")
        settings = read_file()

        if len(new_word) < 2:
            print("Word should be of minimum 2 characters")
            sleep(1)
            return self.add_word()

        if new_word.lower() in settings["words"]["easy"] or new_word.lower() in settings["words"]["medium"] or new_word.lower() in settings["words"]["hard"]:
            print(f"{new_word} already exists in the dictionary")
            sleep(1)
            return self.add_word()

        if not new_word.isalpha():
            print("Word should contain only alphabets")
            sleep(1)
            return self.add_word()

        if 2 <= len(new_word) <= 4:
            settings["words"]["easy"].append(new_word.lower())
            print(f"{new_word} added to easy list")
        elif 5 <= len(new_word) <= 6:
            settings["words"]["medium"].append(new_word.lower())
            print(f"{new_word} added to medium list")
        else:
            settings["words"]["hard"].append(new_word.lower())
            print(f"{new_word} added to hard list")

        self.words = settings["words"]
        save_file(settings)

    def remove_word(self):
        word = input("Enter the word: ")
        settings = read_file()
        for key in settings["words"]:
            if word.lower() in settings["words"][key]:
                settings["words"][key].remove(word.lower())
                print(f"{word} removed from {key} list")
                break
        else:
            print(f"{word} not found in any list")
        self.words = settings["words"]
        save_file(settings)

    def view_score(self):
        print(f"Win: {self.score['win']}")
        print(f"Lost: {self.score['lost']}")
        print(f"Total: {self.score['win'] + self.score['lost']}")
        input("Press Enter to continue")

    def set_score(self, state):
        settings = read_file()
        settings["score"][state] += 1
        self.score = settings["score"]
        save_file(settings)

    def reset_score(self):
        settings = read_file()
        settings["score"] = {"win": 0, "lost": 0}
        self.score = settings["score"]
        save_file(settings)
        print("Score reset!!")

