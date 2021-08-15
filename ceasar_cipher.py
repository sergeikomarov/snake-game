alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


text = input("Enter a word:\n").lower()
shift_number = int(input("Enter shift number: "))

def encrypt(plain_text, shift_n):
    cipher = ""
    for letter in plain_text:
        word_index = alphabet.index(letter)
        new_word = word_index + shift_n
        cipher += alphabet[new_word]
    print(cipher)

encrypt(text, shift_number)