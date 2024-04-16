
#generates encryption key
def generate_key(text, key):
    key = list(key)
    #checks to see if the keyword length is the same as the text length
    if len(text) == len(key):
        return(key)
    else:
        #if not, repeats the letters of the keyword to match the text length
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

#encrypts the text
def vigenere_cipher(text, key):
    cipher_text = []
    for i in range(len(text)):
        char = text[i]
        #checks is the character is a space and replaces it with a space
        if char == ' ':
            cipher_text.append(' ')
        else:
            #converts the letters into its unicode number and adds the 
            #code of the original letter and the key, but ensures it doesn't go over 26 
            letter = (ord(char) + ord(key[i])) % 26
            #adds the number to the unicode of A
            letter += ord('A')
            #converts unicode number back to a letter
            cipher_text.append(chr(letter))
    return("" . join(cipher_text))

#actual program
print("Welcome to the Vigenère Encryptor")
decrypted_text = input("Enter text here: ")
keyword = input("Enter encryption keyword: ")

key = generate_key(decrypted_text, keyword)
encrypted_text = vigenere_cipher(decrypted_text, key)

print("Encrypted text = ", encrypted_text)

