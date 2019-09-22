"""Takes a word and forms it's pig latin equivalent."""

def pigify():
    """Take first letter of word, adds it to the end, and adds 'ay'."""
    while True:
        word = input("Choose a word to pigify\n")
        print("\n\n")
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        if word[0] not in vowels:
            print(word[1:] + word[0] + 'ay')
        else:
            print(word + 'way')
        try_again = input("\nAgain?\n")
        if try_again.lower() == "n":
            break
    input("\nPress Enter to exit.")

if __name__ == "__main__":
    pigify()
