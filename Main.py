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
    text = input("Enter a word: ")
    print(f'In pig latin, your text would be {pig_latin(text)}')