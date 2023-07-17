from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value
        
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)
    
class Phone(Field):
    pass

class Name(Field):
    pass
# 
# class Phone(Field):
#     pass


class Record():
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
    
    def add_phone(self, phone: Phone):
        self.phones.append(phone)
        return f'Contact {self.name} was updated with phone {phone}'
    
    def __str__(self) -> str:
        return f"{self.name}: {', '.join(str(p) for p in self.phones)}"
#     def add_phone(self, *phones):
#         for phone in phones:
#             self.contacts.append(phone)
# 
#     def del_phone(self, *phones):
#         for phone in phones:
#             if phone in self.contacts:
#                 self.contacts.delete(phone)
# 
#     def change_phone(self, old, new):
#         if old in self.contacts:
#             self.contacts.delete(old)
#             self.contacts.append(new)
            
    
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} was added"
    
    def __str__(self) -> str:
        return '\n'.join(str(r) for r in self.values())



