string = input() + ' '

en_lower = 'abcdefghijklmnopqrstuvwxyz'
en_upper = en_lower.upper()


def crypto(string):
    string_out = ''
    count = 0
    n = 0
    for i in range(len(string)):
        if string[i].isalpha() == True:
            count += 1
            continue
        else:
            for k in string[n:i]:
                if k == k.upper():
                    j = en_upper.find(k)
                    if j != -1:
                        j = (j + count) % 26
                        string_out += en_upper[j]
                else:
                    j = en_lower.find(k)
                    if j != -1:
                        j = (j + count) % 26
                        string_out += en_lower[j]
            string_out += string[i]
        count = 0
        n = i + 1
    return string_out[:-1]


print(crypto(string))