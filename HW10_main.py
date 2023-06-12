from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def del_record(self, name):
        if name in self:
            self.data.pop(name)
        else:
            print('bot>> Error. This record does not exist!')

    def show_all(self):
        print(f'bot>> {list(self.data)}')

class Record:
    def __init__(self, name, phone=None):
        self.name = name
        if phone:
            self.phones = []
            self.phones.append(phone)

    def add_new_phone(self, new_phone):
        if not phone:
            self.phones = []
            self.phones.append(new_phone)
        else:
            self.phones.append(new_phone)

    def del_phone(self, phone=''):
        if not phone:
            self.phones.pop()  #delete the last
        else:
            if phone in self.phones:
                self.phones.remove(phone)
            else:
                print('bot>> Error. This phone does not exist!')

class Field:
    pass


class Name(Field):
    def __init__(self, value):
        # super().__init__()
        self.value = value


class Phone(Field):
    def __init__(self, value):
        # super().__init__()
        self.value = value

    
if __name__ == "__main__":
    pass
