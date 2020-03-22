def reverseWords(s):
    c = []
    # s = s.strip()
    # words = s.split(' ')
    words = s.strip().split()

    for word in words:
        c.insert(0, word)
    return ' '.join(c)

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world!  "))
print(reverseWords("a good   example"))