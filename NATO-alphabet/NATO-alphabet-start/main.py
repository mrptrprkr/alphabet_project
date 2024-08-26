import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word:").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

while True:
    # main program
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        word = input("Enter a word:").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    else:
        print("Goodbye")
        break
        