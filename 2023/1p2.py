import os
import re

def solution(lines):
    sum = 0
    # Mapping number words to their respective integer values
    word_to_number = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    target_words = list(word_to_number.keys())  # List of target words

    for line in lines:
        matches = []
        i = 0

        # Scan through the line to find matches for target words
        while i < len(line):
            for word in target_words:
                if line[i:i+len(word)] == word:  # Match the word at current position
                    matches.append(word)
                    i += len(word) - 1  # Move index to end of found word
                    break
            i += 1

        # If at least two words are found, combine the first and last found numbers
        if len(matches) >= 2:
            first_number = word_to_number[matches[0]]
            last_number = word_to_number[matches[-1]]
            combined_number = int(f"{first_number}{last_number}")
            sum += combined_number

    return sum


Input = input("Enter Y2023 S1 P2 Target file: ")

with open(Input, 'r') as file:
    list = file.read()

print(solution(list.split()))