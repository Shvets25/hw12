import pickle

# Клас для представлення контакту
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# Клас для адресної книги
class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)

    def save_to_disk(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_disk(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            self.contacts = []

    def search_contacts(self, search_term):
        matching_contacts = []
        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.phone:
                matching_contacts.append(contact)
        return matching_contacts

# Головна функція
def main():
    address_book = AddressBook()
    address_book.load_from_disk('address_book.pkl')  # Завантаження даних з файлу

    while True:
        print("1. Додати контакт")
        print("2. Пошук контакту")
        print("3. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            address_book.add_contact(name, phone)
            address_book.save_to_disk('address_book.pkl')  # Збереження даних на диск
        elif choice == '2':
            search_term = input("Введіть пошуковий запит: ")
            matching_contacts = address_book.search_contacts(search_term)
            if matching_contacts:
                for contact in matching_contacts:
                    print(f"Ім'я: {contact.name}, Номер телефону: {contact.phone}")
            else:
                print("Контактів не знайдено.")
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
