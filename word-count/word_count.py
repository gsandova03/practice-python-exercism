import string

def count_words(sentence):

    punt = string.punctuation

    for c in punt:
        sentence = sentence.replace(c, "")

    palabras = sentence.lower().split()
    apariciones = []

    print( palabras )
    for palabra in palabras:
        apariciones.append(int(palabras.count( palabra )))

    word_count = dict( zip( palabras, apariciones ) )
    return word_count
