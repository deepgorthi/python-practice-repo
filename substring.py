#!/usr/bin/env python3

def set_of_substrings(input_string):
    for i in range(len(input_string)):
        for j in range(i+1, len(input_string)+1):
            print(input_string[i:j])

set_of_substrings("abccba")