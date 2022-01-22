import sys


russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
other_symbols = "()-+=[]{}|/<>,.'0123456789!@#$%^&*;: \n«—?»’"


# словарь частот русского алфавита
frequency_ru_letter = {"о": 0.10983, "е": 0.07998, 'ё': 0.00013, "а": 0.08483, "и": 0.07367,
    "т":0.067, "н": 0.06318, "с": 0.05473, "р": 0.04746, "в": 0.04343, "л": 0.04533, "к": 0.03486,
    "м": 0.02977, "д": 0.03203, "п": 0.02615, "у": 0.02804, "я": 0.02001, "ы": 0.01735, "з": 0.01687,
    "ь": 0.01641, "ъ": 0.00037	, "б": 0.01592, "г": 0.01898, "ч": 0.0145, "й": 0.0094, "х": 0.00966,
    "ж": 0.01208, "ю": 0.00639, "ш": 0.00718, "ц": 0.00486, "щ": 0.00361, "э": 0.00331, "ф": 0.00267
}


def generate_alphabet_for_caesar(key, keyword):
    delimiter = key
    caesar_alphabet = russian_alphabet[len(russian_alphabet) - delimiter:] + russian_alphabet[:len(russian_alphabet) - delimiter]
    for char in keyword:
        caesar_alphabet = caesar_alphabet.replace(char, "")
    caesar_alphabet = caesar_alphabet[:delimiter] + keyword + caesar_alphabet[delimiter:]
    return caesar_alphabet


def encript_caesar(key, keyword, text):
    """функция кодирования текста шифром цезаря"""
    encript_text = ""
    key = key % len(russian_alphabet)
    caesar_alphabet = generate_alphabet_for_caesar(key, keyword)

    for _, ch in enumerate(text):
        if ch in other_symbols:
            encript_text += ch
        else:
            try:
                encript_text += caesar_alphabet[(caesar_alphabet.index(ch.lower()) + key) % len(caesar_alphabet)]
            except ValueError:
                print("Такого символа нет в русском алфавите")
                print(ch)
                sys.exit(-1)

    return encript_text


def get_frequency_rus_letter_in_text(text):
    "функция для посчета частот для каждой русской буквы в тексте"
    frequency_rus_letter_in_text = {}
    for letter in russian_alphabet:
        frequency_rus_letter_in_text[letter] = 0

    count = 0
    for letter in text:
        if letter in russian_alphabet:
            count += 1
            frequency_rus_letter_in_text[letter] += 1

    for key in frequency_rus_letter_in_text.keys():
        frequency_rus_letter_in_text[key] = [frequency_rus_letter_in_text[key] / count]
    return frequency_rus_letter_in_text


def sort_frequency_dictionary(frequency_rus_letter_in_text):
    """возвращает список русских букв по убыванию их частот"""
    return sorted(frequency_rus_letter_in_text, key=frequency_rus_letter_in_text.get, reverse=True)


def decript_text_by_frequency_analysis(text):
    """функция для расшифровки текста частотным анализом """
    decript_text = ""
    get_list_symbols_frequency_encript_text = sort_frequency_dictionary(get_frequency_rus_letter_in_text(encript_text))
    get_frequency_list_rus_symbols = sort_frequency_dictionary(frequency_ru_letter)
    for _, ch in enumerate(text):
        if ch in other_symbols:
            decript_text += ch
        else:
            char = get_frequency_list_rus_symbols[get_list_symbols_frequency_encript_text.index(ch)]
            decript_text += char
    return decript_text


if __name__ == "__main__":
    with open("война_и_мир.txt", "r", encoding="utf-8") as file:
        text = file.read()
    key = int(input("Введите ключ k: "))
    keyword = input("Введите ключевое слово в котором все буквы различны: ")
    encript_text = encript_caesar(key, keyword, text)
    print(encript_text)
    print("\n\n\n\n")
    print(decript_text_by_frequency_analysis(encript_text))
