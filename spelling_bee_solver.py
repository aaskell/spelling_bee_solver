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

def find_words(word_list, letter_list, essential_letter):
    found_words_all = []
    found_words = []
    for word in word_list:
        if all([letter in letter_list for letter in word]):
            found_words_all.append(word)
    for word in found_words_all:
        if len(word) > 3 and any([letter in essential_letter for letter in word]):
            found_words.append(word)
    return found_words

letter_list = []
for i in range(0, 7):
    letter = (input(f"Letter {i+1}: ").lower())
    letter_list.append(letter)

essential_letter = list(input(f"Essential letter: ").lower())

print(find_words(word_list, letter_list, essential_letter))