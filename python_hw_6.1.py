import string


input_str = input('Please, enter two letters hyphenated: ').split('-')

starting = string.ascii_letters.find(input_str[0])
ending = string.ascii_letters.find(input_str[-1])

print(string.ascii_letters[starting:ending + 1])
