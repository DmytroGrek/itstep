# Напишіть функцію beautiful_list_generator, що приймає список, символ (маркер)
# та назву файлу. Функція створить файл з назвою, що в неї передали і маркером
# та помістить цей список в сприйнятний для більшості формі.
def beautiful_list_generator(lst: list, marker: str, file_name: str) -> bool:
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            for i in lst:
                f.write(marker + ' ' + i + '\n')
            return True
    except:
        return False


if __name__ == "__main__":
    dc_heroes = [
        "Batman",
        "Superman",
        "Flash",
        "Green Lantern",
        "Wonder Woman",
    ]
    print(beautiful_list_generator(dc_heroes, "\u2713", "heroes.txt"))
