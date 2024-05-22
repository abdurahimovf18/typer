
import keyboard as kb
from text import Text
import string
import os
from colors import colored, reset


class App(object):
    def __init__(self):
        self.text = Text(self)
        self.mistakes = 0
        self.last_wpm = 0
        self.logic = {
            "1": self.text.set_configurations,
            "2": self.text.set_settings
        }
        self.barrier_color = "yellow"
        self.text_color = "cyan"
        self.info_color = "cyan"
        self.info_info_color = "blue"
        self.keydown = set()

    def execute_new_pressing(self, letters: set):
        [self.text.execute(letter) for letter in letters if letter not in self.keydown]
        self.keydown = letters

    def run(self):
        while True:
            if self.text.texting:
                # keyboard handling
                self.execute_new_pressing({letter for letter in string.ascii_letters + " " if kb.is_pressed(letter)})
                [self.logic[letter]() for letter in self.logic.keys() if kb.is_pressed(letter)]

                # looking for changes
                if not self.text.change:
                    continue

                self.text.change = False

                # showing
                os.system("cls")
                print("\n" * 3)
                enter = "\n"

                barrier_se = colored("|", self.barrier_color)
                last = colored("Last", self.info_info_color)
                l_wpm = colored("-WPM", self.info_info_color)
                last_wpm = colored(str(self.last_wpm), self.info_color)
                b = colored("&", self.barrier_color)
                mistakes = colored("-Mistakes", self.info_info_color)
                mistakes_info = colored(str(self.mistakes), self.info_color)
                current_wpm = colored("Current WPM", self.info_info_color)
                c_wpm = colored(str(self.text.wpm), self.info_color)
                word_count = colored("Word Count", self.info_info_color)
                w_count = colored(str(self.text.word_count), self.info_color)

                text = f"""
{last} \t{l_wpm}: {last_wpm} {b} {mistakes}: {mistakes_info} \t{barrier_se}\t{current_wpm}: {c_wpm} \t{barrier_se}\t {word_count}: {w_count}


{colored("1.", "white")} {colored("Next Text", self.info_color)}
{colored("2.", "white")} {colored("Set Configurations", self.info_color)}

{enter * 7}
    
{self.text.show_text}{reset()}"""
                print(text)

    def set_wpm(self, wpm: float):
        self.last_wpm = wpm

    def set_mistakes(self, mistakes: int):
        self.mistakes = mistakes


if __name__ == '__main__':
    App().run()
