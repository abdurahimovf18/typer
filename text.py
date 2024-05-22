
from colors import colored
import time
import os
from random import choice


class Text(object):
    def __init__(self, app):
        self.change = False
        self.words = ["word", "against", "now", "never", "along", "usual", "day", "morning", "exception", "already",
                      "nothing", "zero", "point", "people", "almost", "there", "queue", "ask", "question", "bee",
                      "see", "python", "like"]
        self.mistakes = 0
        self.last_mistake = ""
        self.app = app
        self.text: str = ...
        self.wpm: float = ...
        self.start_time: float = ...
        self.word_count = 25
        self.show_for = 100
        self.show_text: str = ""
        self.texting = True
        self.starting = True
        self.barrier_color = "yellow"
        self.text_color = "cyan"
        self.ic = "cyan"
        self.ec = "yellow"
        self.sc = "green"
        self.settings_logic = {
            "1": self.change_word_length,
            "2": self.add_my_words,
            "3": self.remove_words
        }

        self.set_configurations()

    def set_configurations(self) -> None:
        self.set_text(self.word_count)
        self.wpm = 0
        self.mistakes = 0
        self.start_time = time.perf_counter()
        self.set_show_text()
        self.change = True

    @staticmethod
    def new_settings_iter(info: str):
        time.sleep(0.3)
        os.system("cls")
        print(info)

    def set_settings(self):
        self.texting = False

        info_text = colored("Settings ...\n", "blue")+colored("""
1. change word length
2. Add my words
3. Remove words
0. quit settings
""", self.ec)
        while True:
            self.new_settings_iter(info_text)
            operation = input(colored("Enter the operation: ", self.ic))

            if operation == "0":
                self.texting = True
                self.set_configurations()
                break

            elif operation in self.settings_logic:
                self.settings_logic[operation]()

            self.set_configurations()

    def remove_words(self):
        word = input(colored("Enter the word: ", self.ic))
        if word in self.words and len(self.words) > 1:
            self.words.remove(word)

        print(colored("Success, word has been removed!", self.sc))

    def change_word_length(self):
        wrong_input = colored("Wrong input!", "red")
        self.word_count = int(input(colored("Enter the word count: ", self.ic)))
        if self.word_count < 1:
            self.word_count = 50
            print(wrong_input)

    def add_my_words(self):
        wrong_input = colored("Wrong input!", "red")
        word = input(colored("Enter the word: ", self.ic))
        if word not in self.words and word.isalpha():
            self.words.append(word)
            self.set_configurations()
            print(colored("Success, word has been added!", self.sc))
        else:
            print(wrong_input)

    def set_text(self, words_limit: int = 50) -> None:
        self.text = " ".join(choice(self.words) for _ in range(words_limit))

    def set_wpm(self):
        writen_length = self.word_count - len(self.text.split()) + 1
        interval_time = (time.perf_counter() - self.start_time) / 60
        self.wpm = round(writen_length / interval_time, 2)

    def execute(self, letter: str):
        last = self.wpm
        last_mistakes = self.mistakes
        self.set_wpm()

        if self.text == "":
            self.set_configurations()
            self.app.set_wpm(wpm=last)
            self.app.set_mistakes(mistakes=last_mistakes)

        elif self.text[0] == letter:
            self.change = True
            if self.starting:
                self.starting = not self.starting
                self.start_time = time.perf_counter()

            self.text = self.text[1:]
        else:
            self.mistakes += 1

        self.set_show_text()

    def set_show_text(self):
        t = f"{self.text[:self.show_for - 3]}{' ' * (self.show_for - len(self.text) - 3)}"

        c_text = colored(f"{t}..." if len(self.text) > self.show_for else f"{t}   ", self.text_color)
        barrier = colored(f"+{'-' * self.show_for}+", self.barrier_color)
        barrier_se = colored("|", self.barrier_color)
        self.show_text = f"""
{barrier}
{barrier_se}{c_text}{barrier_se}
{barrier}"""
