"""task 02"""


def get_cats_info(path) -> list[dict[str, str]]:
    """
    Reads a file containing information about cats and returns a list of dictionaries,
    each representing a cat. The function handles exceptions for file not found and
    incorrect data formatting.

    Parameters:
    - path (Path): The path to the file containing cat data. The file should be in CSV format,
      where each line contains the ID, name, and age of a cat, separated by commas.

    Returns:
    - List[Dict[str, str]]: A list of dictionaries. Each dictionary contains the following keys:
      - 'id': The ID of the cat.
      - 'name': The name of the cat.
      - 'age': The age of the cat.

    Exceptions:
    - FileNotFoundError: Raised if the file is not found at the specified path. In this case,
      an error message is printed.
    - ValueError: Raised if a line in the file does not contain exactly three values (ID, name, age).
      In this case, an error message is printed and the line is skipped.
    """
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(",")
                    cats.append({"id": id, "name": name, "age": age})
                except ValueError:
                    print("Info about cat is incorrect")
    except FileNotFoundError:
        print(f"File {path} not found")

    return cats


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
