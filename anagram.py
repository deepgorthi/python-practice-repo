from collections import Counter

def anagram(str1, str2):
    str1_counter = Counter(str1)
    str2_counter = Counter(str2)
    print(f"str1_counter is {str1_counter}")
    print(f"str2_counter is {str2_counter}")
    if str1_counter == str2_counter:
        return "True"

print(anagram('abc','bca'))
