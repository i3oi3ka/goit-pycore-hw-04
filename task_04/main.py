"""task 04"""


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts) -> str:
    name, phone = args
    if contacts.get(name):
        contacts[name] = phone
        return f"Contact {name} updated."
    else:
        return f"Name {name} not found, please choose command: 'add contact'."


def show_phone(args, contacts) -> str:
    name = args[0]
    if contacts.get(name):
        return f"{contacts[name]}"
    else:
        return f"Name {name} not found."


def show_all(contacts) -> None:
    if not contacts:
        return "Sorry, your phone book is empty."
    else:
        all_contacts = ""
        for name, phone in contacts.items():
            all_contacts += f"{name:<20} - {phone}\n"
        return all_contacts.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
