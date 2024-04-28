def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."
def show_phone(name, contacts):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."
def show_all(contacts):
    if contacts:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "No contacts found."



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter command: ")
        cmd, args = parse_input(user_input)
        if cmd == "hello":
            print("How can I help you?")
        elif cmd == "add" and len(args) == 2:
            print(args, contacts)
        elif cmd == "change" and len(args) == 2:
            print(change_contact(args[0], args[1], contacts))
        elif cmd == "phone" and len(args) == 1:
            print(show_phone(args[0], contacts))
        elif cmd == "all" and len(args) == 0:
            print(show_all(contacts))
        elif cmd in ["close", 'exit']:
            print("Good bye!")
            exit()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
