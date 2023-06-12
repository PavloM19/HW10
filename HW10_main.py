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
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    AB = AddressBook()
    AB.add_record(rec)
    assert isinstance(AB['Bill'], Record)
    assert isinstance(AB['Bill'].name, Name)
    assert isinstance(AB['Bill'].phones, list)
    assert isinstance(AB['Bill'].phones[0], Phone)
    assert AB['Bill'].phones[0].value == '1234567890'
    print('All Ok)')

    # name2 = Name('John')
    # phone2 = Phone('51646516546')
    # rec2 = Record(name2, phone2)
    # AB.add_record(rec2)

    # AB.show_all()
    # # AB.del_record('Bill')
    # # AB.show_all()

    # print(phone2.value)
    # print(AB['Bill'].phones)
    # print(rec2.phones[0].value)