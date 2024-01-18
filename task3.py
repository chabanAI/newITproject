def count_letters(text):

    letter_counter = {}
    for char in text:
        if char.isalpha() and char.islower():
            letter_counter[char] = letter_counter.get(char, 0) + 1
    return letter_counter

def calculate_frequency(letter_counter):
    
    total_letter_count = sum(letter_counter.values())
    frequencies = {letter: count / total_letter_count for letter, count in letter_counter.items()}
    return frequencies

def print_frequencies(frequencies):
    
    for letter, frequency in frequencies.items():
        print(f"{letter}: {frequency:.2f}")

text = "This is an example text for letter frequency analysis. The text may contain various symbols, but we are interested only in letters."
letter_counter = count_letters(text)
frequencies = calculate_frequency(letter_counter)

print_frequencies(frequencies)
