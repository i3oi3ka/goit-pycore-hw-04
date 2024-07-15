"""task 03"""

import sys
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def print_directory_contents(path: Path, prefix: str = ""):
    """
    Recursively prints the directory structure with color formatting.

    Args:
    - path (Path): The path to the directory.
    - prefix (str, optional): Prefix string for indentation. Defaults to ''.
    """
    try:
        for item in path.iterdir():
            if item.is_dir():
                # Print directory name in blue color
                print(f"{prefix}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                # Recursive call for subdirectory
                print_directory_contents(item, prefix + "    ")
            else:
                # Print file name in green color
                print(f"{prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        # Handle permission error
        print(f"{prefix}{Fore.RED}Permission denied: {item}{Style.RESET_ALL}")


if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python hw03.py <path_to_directory>")
        sys.exit(1)

    # Get directory path from command line argument
    dir_path = Path(sys.argv[1])

    # Check if path exists and is a directory
    if not dir_path.exists():
        print(f"Error: The path '{dir_path}' does not exist.")
        sys.exit(1)
    if not dir_path.is_dir():
        print(f"Error: The path '{dir_path}' is not a directory.")
        sys.exit(1)

    # Print directory structure
    print(f"{Fore.CYAN}{dir_path}{Style.RESET_ALL}")
    print_directory_contents(dir_path)
