from collections import UserDict

class Field:
    pass

class Name(Field):
    def __init__(self, value):
        self.name = value


class Phone(Field):
    def __init__(self, value):
        self.phone = value
        
        
class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.name] = record
    
    def del_record(self, name):
        if self.data.pop(name, None):
            f'Contact {name} was removed from addres book.'
        return f'There is no {name} in address book to delete.'
        


    def get_phones(self):
        return self.data.get('phones')
    
    def add_record(self, record):
        self.data[record.name.name] = record
        

addressbook = AddressBook()

class Record():
    contacts = []
    def __init__(self, name, *phones):
        self.name = name
        self.contacts.append(phones)
     

        
def add(args = ('Alex', '012345687', '123456489', '4562')):#args: tuple[str]) -> str:
    name = Name(args[0])
    phone = Phone(args[1:])
    rec = Record(name, phone)
    return addressbook.add_record(rec)

rec = add()
rec = add(('Alex1', '0123', '123489'))
print(addressbook)
print(addressbook.del_record('Alex1'))



def input_error(func):
    def wrapper(*args):
        try:
            result = func(args)
        except Exception as err:
            if err:
                if func.__name__ == 'show_phone':
                    return f'Input name after command "phone"'
                return f'Input name and phone number after command "{func.__name__}"'

        return result
    return wrapper


@input_error
def add(args: tuple[str]) -> str:
    name = Name(args[0])
    phone = Phone(args[1])
    rec = Record(name, phone)
    return addressbook.add_rec(rec)


@input_error
def change(args: tuple[str]) -> str:
    name = args[0]
    phone = args[1]
    phone_book[name] = phone
    return f"Contact '{name}' was succesfuly updated with phone: {phone}"


@input_error
def show_phone(name: tuple[str]) -> str:
    if name[0] in phone_book:
        return f'{name[0]} has number {phone_book[name[0]]}'
    else:
        return f'There is no phone number for {name[0]}'


def show_all() -> str:
    if phone_book:
        s = ''
        for name, phone in sorted(phone_book.items()):
            s += f'{name}: {phone}'
            s += '\n'
        return s + '...the end of phone book.'
    return 'Phone book is empty'


def no_command():
    return 'Unknown command'


def exits():
    return 'Good bye!'


def hello() -> str:
    return 'How can I help you?'


COMMANDS = {"good bye": exits,
            "close": exits,
            "exit": exits,
            "hello": hello,
            "show all": show_all}


def parser(text: str) -> tuple[callable, tuple[str] | None]:

    if text.startswith('add'):
        return add, text.replace("add", "").strip().split()

    if text.startswith('change'):
        return change, text.replace("change", "").strip().split()

    if text.startswith('phone'):
        return show_phone, text.replace("phone", "").strip().split()

    if text in COMMANDS:
        return COMMANDS[text], None

    return no_command, None


def main():
    print("I am at your service, my lord!")
    while True:
        user_input = input('>>> ')
        command, data = parser(user_input)
        if data is None:
            result = command()
        else:
            result = command(*data)
        print(result)
        if command == exits:
            break


if __name__ == "__main__":
    main()
