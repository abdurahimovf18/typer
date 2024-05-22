from colorama import Fore, Style


data = {
    "black": Fore.BLACK,
    "red": Fore.RED,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "green": Fore.GREEN,
    "white": Fore.WHITE,
    "cyan": Fore.CYAN,
}


def colored(text: str, color: str) -> str:
    text = f"{data.get(color, data['white'])}{text}{Style.RESET_ALL}"
    return text
