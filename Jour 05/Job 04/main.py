def decale_message(message, decalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message_decale = ""
    for lettre in message:
        if lettre in alphabet:
            index = (alphabet.index(lettre) + decalage) % 26
            message_decale += alphabet[index]
        else:
            message_decale += lettre
    return message_decale
message = "hello world"
decalage = 3
message_decale = decale_message(message, decalage)
print(message_decale)