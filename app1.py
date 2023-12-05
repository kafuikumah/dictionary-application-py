import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word does not exist. Please check your spelling"

word = input("Enter word: ")

print(translate(word))