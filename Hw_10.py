from ab_classes import AddressBook, Name, Phone, Record
address_book = AddressBook()

def input_error(func):
    def wrapper(*args):
        try:
            return func(args)
        except Exception as err:
            return err
#              if err:
#                  if func.__name__ == 'show_command':
#                      return 'Input name after command'
#                  return 'Input name and phone number after command'
    return wrapper


@input_error
def add_command(args: tuple[str]) -> str:
    name = Name(args[0])
    phone = Phone(args[1])
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.add_phone(phone)
    rec = Record(name, phone)
    return address_book.add_record(rec)

@input_error
def change_command(args: tuple[str]) -> str:
    pass
#     name = args[0]
#     phone = args[1]
#     phone_book[name] = phone
#     return f"Contact '{name}' was succesfuly updated with phone: {phone}"


@input_error
def show_command(name: tuple[str]) -> str:
    pass
#     if name[0] in phone_book:
#         return f'{name[0]} has number {phone_book[name[0]]}'
#     else:
#         return f'There is no phone number for {name[0]}'


def show_all_command(*args) -> str:
    return address_book
#     if phone_book:
#         s = ''
#         for name, phone in sorted(phone_book.items()):
#             s += f'{name}: {phone}'
#             s += '\n'
#         return s + '...the end of phone book.'
#     return 'Phone book is empty'


def no_command():
    return 'Unknown command'


def exit_command():
    return 'Good bye!'


def hello_command() -> str:
    return 'How can I help you?'


COMMANDS = {
    add_command: ('add', '+', 'додати'),
    change_command: ('change', 'змінити'),
    exit_command: ('close', 'exit', 'вийти' 'закрити'),
    hello_command: ('hello', 'привіт'),
    show_command: ('phone', 'show', 'телефон'),
    show_all_command: ('show_all', 'show all', 'all', 'всі', 'телефони')
    }
        
def parser(text: str) -> tuple[callable, list[str]]:
    command, *data = text.strip().split()
    for cmd, kwds in COMMANDS.items():
        if command.lower() in kwds:
            return cmd, data
    return no_command, []


def main():
    print("I am at your service, my lord!")
    while True:
        user_input = input('>>> ')
        command, data = parser(user_input)
        result = command(*data)
        print(result)
        if command == exit_command:
            break


if __name__ == "__main__":
    main()
