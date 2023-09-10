import os

# Путь к директории для хранения заметок
NOTE_DIRECTORY = "notes"

# Создаем директорию для заметок, если она не существует
if not os.path.exists(NOTE_DIRECTORY):
    os.makedirs(NOTE_DIRECTORY)

def create_note(note_title, note_content):
    """
    Создает новую заметку.

    :param note_title: Заголовок заметки.
    :param note_content: Содержание заметки.
    """
    note_filename = os.path.join(NOTE_DIRECTORY, note_title + ".txt")
    with open(note_filename, "w") as note_file:
        note_file.write(note_content)

def read_notes():
    """
    Возвращает список всех доступных заметок.

    :return: Список заметок в виде словаря, где ключ - заголовок, значение - содержание.
    """
    notes = {}
    for note_filename in os.listdir(NOTE_DIRECTORY):
        with open(os.path.join(NOTE_DIRECTORY, note_filename), "r") as note_file:
            note_title = os.path.splitext(note_filename)[0]
            note_content = note_file.read()
            notes[note_title] = note_content
    return notes

def edit_note(note_title, new_content):
    """
    Редактирует существующую заметку.

    :param note_title: Заголовок заметки, которую нужно отредактировать.
    :param new_content: Новое содержание заметки.
    """
    note_filename = os.path.join(NOTE_DIRECTORY, note_title + ".txt")
    if os.path.exists(note_filename):
        with open(note_filename, "w") as note_file:
            note_file.write(new_content)
    else:
        print("Заметка с указанным заголовком не найдена.")

def delete_note(note_title):
    """
    Удаляет существующую заметку.

    :param note_title: Заголовок заметки, которую нужно удалить.
    """
    note_filename = os.path.join(NOTE_DIRECTORY, note_title + ".txt")
    if os.path.exists(note_filename):
        os.remove(note_filename)
    else:
        print("Заметка с указанным заголовком не найдена.")

if __name__ == "__main__":
    while True:
        print("\nВыберите действие:")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            note_title = input("Введите заголовок заметки: ")
            note_content = input("Введите содержание заметки: ")
            create_note(note_title, note_content)
            print("Заметка создана успешно.")
        elif choice == "2":
            notes = read_notes()
            if notes:
                print("\nСписок заметок:")
                for title, content in notes.items():
                    print(f"Заголовок: {title}")
                    print(f"Содержание: {content}")
                    print("-" * 20)
            else:
                print("Заметок пока нет.")
        elif choice == "3":
            note_title = input("Введите заголовок заметки для редактирования: ")
            new_content = input("Введите новое содержание заметки: ")
            edit_note(note_title, new_content)
            print("Заметка отредактирована успешно.")
        elif choice == "4":
            note_title = input("Введите заголовок заметки для удаления: ")
            delete_note(note_title)
            print("Заметка удалена успешно.")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите корректное действие.")

