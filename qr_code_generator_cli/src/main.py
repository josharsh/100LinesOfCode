import typer
import pyqrcode
from rich.prompt import Prompt
from rich.progress_bar import ProgressBar

from utils import *

def main():
    main_screen()
    url = pyqrcode.create(get_url_prompt())
    save = get_save_option()
    
    if save == 'n':
        text = url.text()
        with open(string_generator() + ".txt", 'w') as f:
            f.write(text)
    elif save == 'y':
        url.svg(string_generator() + ".svg", scale=8)
    else:
        print("[bold red]Invalid response![/bold red]")
        return main()



if __name__ == "__main__":
    typer.run(main)