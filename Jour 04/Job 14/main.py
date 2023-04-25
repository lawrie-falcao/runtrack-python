def my_long_word(n, string):
    words = string.split()
    long_words = [word for word in words if len(word) > n]
    return " ".join(long_words)
sentence = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
long_words = my_long_word(3, sentence)
print(long_words)
