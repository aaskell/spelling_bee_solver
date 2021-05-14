import requests

url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'
resp = requests.get(url)
with open('word_list.txt', 'wb') as f:
    f.write(resp.content)

word_list_file = open("word_list.txt", "r")
word_list_raw = []
for word in word_list_file:
    word_list_raw.append(word)
word_list = [x.replace('\n', '') for x in word_list_raw]

letter_list = []

essential_letter = input(f"Essential letter: ").lower()
while not essential_letter.isalpha() or len(essential_letter)!=1:
    print("Invalid input - try again.")
    essential_letter = input(f"Essential letter: ").lower()

letter_list.append(essential_letter)

for i in range(0, 6):
    letter = (input(f"Letter {i+1}: ").lower())
    while not letter.isalpha() or len(letter)!=1 or letter in letter_list:
        print("Invalid input - try again.")
        letter = input(f"Letter {i+1}: ").lower()
    letter_list.append(letter)

def find_words(word_list, essential_letter, letter_list):

    found_words_all = []
    found_words = []
    pangrams = []

    for word in word_list:
        if all([letter in letter_list for letter in word]):
            found_words_all.append(word)
    for word in found_words_all:
        if len(word) > 3 and any([letter in essential_letter for letter in word]):
            found_words.append(word)
        if set(word) == set(letter_list):
            pangrams.append(word)
        

    total = len(found_words)

    score = 0

    for word in found_words:
        if len(word)==4:
            score+=1
        elif word not in pangrams:
            score+=len(word)
        else:
            score+=len(word) + 7

    print(f'\n Words found: {found_words}')
    if pangrams:
        print(f'\n Pangrams found: {pangrams}')
    else:
        print(f'\n No pangrams found.')
    print(f'\n Total words found: {total}')
    if pangrams:
        print(f'\n Total pangrams found: {len(pangrams)}')
    print(f'\n Total score: {score}\n')

    return found_words, total, score, pangrams

find_words(word_list, essential_letter, letter_list)

