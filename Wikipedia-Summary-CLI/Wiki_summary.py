import wikipedia
import sys

# ANSI colors for terminal styling
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

BANNER = f"""{CYAN}{BOLD}

-----

\\ \\      / (*) | *(*)* __   ___  ___  | (*)
 \\ \\ /\\ / /| | |/ / | '* \\ / _ \\ **| | | |
  \\ V  V / | |   <| | |*) |  _*/_* \\ | | |
   \\_/\\_/  |*|_|\\_\\_| .**/ \\_**||***/ |*|*|
                    |*|  Summary CLI
{RESET}"""

def search_and_summarize(query: str, sentences: int = 3) -> None:
    print(f"\n{YELLOW}Searching for:{RESET} {query}\n")
    try:
        # Auto-suggest if query is ambiguous
        results = wikipedia.search(query, results=5)
        if not results:
            print(f"{RED}No results found for '{query}'.{RESET}")
            return

        # Try fetching the top result
        try:
            summary = wikipedia.summary(results[0], sentences=sentences)
            page = wikipedia.page(results[0])
            print(f"{CYAN}{BOLD}>>> {page.title}{RESET}")
            print(f"{GREEN}{summary}{RESET}")
            print(f"\n{YELLOW}Read more:{RESET} {page.url}")

        except wikipedia.exceptions.DisambiguationError as e:
            # Multiple matches - show top 5 options
            print(f"{YELLOW}Multiple matches found. Did you mean:{RESET}")
            for i, option in enumerate(e.options[:5], 1):
                print(f"  {i}. {option}")
            choice = input(f"\n{CYAN}Enter number to select (or 0 to cancel): {RESET}").strip()
            if choice.isdigit() and 1 <= int(choice) <= 5:
                selected = e.options[int(choice) - 1]
                summary = wikipedia.summary(selected, sentences=sentences)
                page = wikipedia.page(selected)
                print(f"\n{CYAN}{BOLD}>>> {page.title}{RESET}")
                print(f"{GREEN}{summary}{RESET}")
                print(f"\n{YELLOW}Read more:{RESET} {page.url}")

    except wikipedia.exceptions.PageError:
        print(f"{RED}Page not found. Try a different search term.{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def main() -> None:
    print(BANNER)

    # Accept query from CLI args or interactive prompt
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        search_and_summarize(query)
        return

    print(f"{YELLOW}Type a topic to search. Commands: 'lines N' = change summary length | 'quit' to exit{RESET}\n")
    sentences = 3  # default summary length

    while True:
        try:
            query = input(f"{CYAN}Search Wikipedia:{RESET} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{GREEN}Goodbye!{RESET}")
            break

        if not query:
            continue
        if query.lower() in ("quit", "exit", "q"):
            print(f"{GREEN}Goodbye!{RESET}")
            break
        if query.lower().startswith("lines "):
            # Allow user to change number of summary sentences
            try:
                sentences = int(query.split()[1])
                print(f"{GREEN}Summary length set to {sentences} sentences.{RESET}")
            except ValueError:
                print(f"{RED}Usage: lines <number>{RESET}")
            continue

        search_and_summarize(query, sentences)
        print()

if __name__ == "__main__":
    main()
