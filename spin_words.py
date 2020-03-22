def spin_words(sentence):
    new_sentence = []
    words = sentence.split()
    for word in words:

        if len(word) >= 5:
            new_sentence.append(str(word[::-1]))
        else:
            new_sentence.append(word)
    return ' '.join(new_sentence)