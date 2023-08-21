import random


def generate_phone_number():
    return f"+7{random.randint(1000000000, 9999999999)}"


def generate_entry():
    first_name = "Иван" + str(random.randint(1, 100))
    last_name = "Петров" + str(random.randint(1, 100))
    patronymic = "Сергеевич" + str(random.randint(1, 100))
    organisation = "Artspray"
    work_phone = generate_phone_number()
    personal_phone = generate_phone_number()
    return f"{first_name},{last_name},{patronymic},{organisation},\
            {work_phone},{personal_phone}"


entries = [generate_entry() for _ in range(100)]

with open("phonebook.csv", "w") as file:
    for entry in entries:
        file.write(entry + "\n")
