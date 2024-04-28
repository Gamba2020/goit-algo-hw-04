def add_contact(username, phone, contacts):
    contacts[username] = phone
    return "Contact added."
def change_contact(username, phone, contacts):
    if username in contacts:
        contacts[username] = phone
        return "Contact updated."
    else:
        return "Contact not found."
def show_phone(username, contacts):
    if username in contacts:
        return contacts[username]
    else:
        return "Contact not found."
def show_all(contacts):
    if contacts:
        result = ""
        for username, phone in contacts.items():
            result += f"{username}: {phone}\n"
        return result
    else:
        return "No contacts found."

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter command: ")
        cmd, args = parse_input(user_input)
        if cmd == "hello":
            print("How can I help you?")
        elif cmd == "add" and len(args) == 2:
            print(add_contact(args[0], args[1], contacts))
        elif cmd == "change" and len(args) == 2:
            print(change_contact(args[0], args[1], contacts))
        elif cmd == "phone" and len(args) == 1:
            print(show_phone(args[0], contacts))
        elif cmd == "all" and len(args) == 0:
            print(show_all(contacts))
        elif cmd == "exit" or cmd == "close":
            print("Good bye!")
            exit()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
