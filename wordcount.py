# from sys import argv


def dict_construct(file_name):
    fhand = open(file_name)

    dict_construct = {}

    for line in fhand:

        words = line.rstrip().split()

        for word in words:
            word = word.lower()
            if not word.isalpha():
                word = word.rstrip(".,,,?")
            #    for letter in word:
            #        word_list = []
            #         if letter.isalpha():
            #             word_list.append(letter)
            #             word = ''.join(word_list)

            dict_construct[word] = dict_construct.get(word, 0) + 1
    return dict_construct


def print_dict(our_dict):
    for key, value in our_dict.items():
        print(key, value)


user_file = input("What file would you like the wordcount of? ")

if len(user_file) < 1: user_file = 'twain.txt'

our_dict = dict_construct(user_file)

print_dict(our_dict)
