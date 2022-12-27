from random import choice

from rich import print
from rich.prompt import Prompt


def main_screen() -> None:
    print("="*32)
    print("||" + (" " * 8) + "[bold red]QR[/bold red] [bold yellow]GENERATOR[/bold yellow]"+ (" " * 8) + "||")
    print("="*32)

def get_url_prompt() -> str:
    url = Prompt.ask("Enter the url?")
    return url

def get_save_option() -> str:
    save = (Prompt.ask("Would you like to save the QR code as svg or txt", default='y')).lower()
    return save

def string_generator() -> str:
    char_list = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
    string = ""
    for i in range(5):
        string += choice(char_list)
    return string