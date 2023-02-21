language = input('Выберите язык алфавита русский "ru" или английский "en"', )
shift = int(input('Введите правую границу n диапазона [0;n]', ))
string = input('Введите строку для шифрования(дешифрования)', )

if language == 'ru' or language == 'кг':
    language_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    language_upper = language_lower.upper()
    language_len = 32
elif language == 'en' or language == 'ут':
    language_lower = 'abcdefghijklmnopqrstuvwxyz'
    language_upper = language_lower.upper()
    language_len = 26

def crypto(language_lower, language_upper, language_len, shift, string):
    string_out = ''
    for i in range(len(string)):
        if string[i].isalpha() == False:
            string_out += string[i]
        if string[i] == string[i].upper():
            j = language_upper.find(string[i])
            if j != -1:
                j = (j - shift) % language_len
                string_out += language_upper[j]
        else:
            j = language_lower.find(string[i])
            if j != -1:
                j = (j - shift) % language_len
                string_out += language_lower[j]
    return string_out

for sh in range(shift + 1):
    print('Сдвиг =', sh, crypto(language_lower, language_upper, language_len, sh, string))