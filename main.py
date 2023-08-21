import os

SPRAVOCHNIK_FILE = "phonebook.csv"


def clear_screen():
    """
    Очистка вывода терминала(clear)
    """
    os.system("clear" if os.name == "posix" else "cls")


def display_entry(entry: list[str]) -> None:
    """
    Вывод всех данных в терминал.
    """
    if entry[0] != "":
        print("Фамилия:", entry[0])
    if entry[2] != "":
        print("Имя:", entry[1])
    print("Отчество:", entry[2])
    if entry[3] != "":
        print("Название организации:", entry[3])
    if entry[4] != "":
        print("Рабочий телефон:", entry[4])
    if entry[5] != "":
        print("Личный телефон:", entry[5])
    print("=" * 40)


def display_page(
    entries: list[list[str]], page_num: int, page_size: int
) -> None:
    """
    Вывод списка контактов в терминал.
    """
    clear_screen()
    print("Телефонный справочник - страница", page_num)
    print("=" * 40)

    start_idx = (page_num - 1) * page_size
    end_idx = start_idx + page_size

    for entry in entries[start_idx:end_idx]:
        display_entry(entry)

    print("=" * 40)


def add_entry(entries) -> None:
    """
    Отображение добавления нового контакта.
    """
    clear_screen()
    print("Добавление новой записи")
    print("=" * 40)

    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    patronymic = input("Отчество: ")
    organization = input("Название организации: ")
    work_phone = input("Рабочий телефон: ")
    personal_phone = input("Личный телефон: ")

    entries.append(
        (
            last_name,
            first_name,
            patronymic,
            organization,
            work_phone,
            personal_phone,
        )
    )
    save_entries(entries)
    print("Запись добавлена!")


def edit_entry(entries: list[list[str]]) -> None:
    """
    Редактирование записи.
    """
    clear_screen()
    search_query = input("Введите фамилию для поиска записи: ")

    matching_entries = search_entries(entries, search_query)

    if not matching_entries:
        print("Запись не найдена.")
        return

    display_page(matching_entries, 1, len(matching_entries))

    entry_index = int(input("Введите номер записи для редактирования: ")) - 1

    if 0 <= entry_index < len(matching_entries):
        clear_screen()
        print("=" * 40)
        display_entry(matching_entries[entry_index])

        field_names = [
            "Фамилия",
            "Имя",
            "Отчество",
            "Название организации",
            "Рабочий телефон",
            "Личный телефон",
        ]

        field_index = (
            int(
                input(
                    """Какое поле отредактировать?
                    1.Фамилия,
                    2.Имя,
                    3.Отчество,
                    4.Название Организации,
                    5.Рабочий телефон,
                    6. Личный телефон
                    """
                )
            )
            - 1
        )

        if 0 <= field_index < len(field_names):
            new_value = input(
                f"Введите новое значение для {field_names[field_index]}: "
            )
            matching_entries[entry_index] = list(matching_entries[entry_index])
            matching_entries[entry_index][field_index] = new_value
            save_entries(entries)
            print("Запись обновлена!")
        else:
            print("Недопустимый номер поля.")
    else:
        print("Недопустимый номер записи.")


def search_entries(entries: list[list[str]], query: str) -> list[list[str]]:
    """
    Поиск по записной книжке.
    """
    return [
        entry
        for entry in entries
        if any(query.lower() in field.lower() for field in entry)
    ]


def save_entries(entries: list[list[str]]) -> None:
    """
    Сохранение записи в файл.
    """
    with open(SPRAVOCHNIK_FILE, "w") as file:
        for entry in entries:
            file.write(",".join(entry) + "\n")


def load_entries():
    """
    Загрузка записей из файла.
    """
    entries = []
    if os.path.exists(SPRAVOCHNIK_FILE):
        with open(SPRAVOCHNIK_FILE, "r") as file:
            for line in file:
                entry = line.strip().split(",")
                entries.append(entry)
    return entries


def main() -> None:
    """
    Логика.
    """
    entries = load_entries()
    page_size = 5
    current_page = 1

    while True:
        display_page(entries, current_page, page_size)

        print("1. Добавить новую запись")
        print("2. Редактировать запись")
        print("3. Поиск записей")
        print("4. Следующая страница")
        print("5. Предыдущая страница")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            edit_entry(entries)
        elif choice == "3":
            search_query = input("Введите строку для поиска: ")
            matching_entries = search_entries(entries, search_query)
            display_page(matching_entries, 1, len(matching_entries))
            input("Нажмите Enter для продолжения...")
        elif choice == "4":
            if current_page < len(entries) / page_size:
                current_page += 1
        elif choice == "5":
            if current_page > 1:
                current_page -= 1
        elif choice == "0":
            break


if __name__ == "__main__":
    main()
