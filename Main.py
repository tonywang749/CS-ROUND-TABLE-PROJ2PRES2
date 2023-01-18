def get_index_first_vowel(input):
    input = input.lower()
    for char in input:
        if char in "aeiou": return input.index(char)
    return None

def pig_latin(input):
    if input[0] in "aeiou":
        input = input + "ay"
    else:
        index = get_index_first_vowel(input)
        input = input[index:] + input[0] + "ay"
    return input

def main():
    text = input("Enter a bunch of words, separated by spaces: ")
    for word in text.split():
        print(f'In pig latin, your word ({word}) would be {pig_latin(word)}')