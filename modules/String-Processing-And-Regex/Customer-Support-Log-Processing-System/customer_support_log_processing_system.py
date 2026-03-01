"""
Implements manual string operations without using built-in
string methods for core logic.
"""


# (a) Find Length Manually
def find_length(text):
    count = 0
    for _ in text:
        count += 1
    return count


# (b) Convert to Uppercase Manually
def convert_to_uppercase(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result


# (c) Check if Two Strings Are Anagrams (Manual Frequency Count)
def are_anagrams(str1, str2):

    if find_length(str1) != find_length(str2):
        return False

    freq = {}

    # Count characters in str1
    for char in str1:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Subtract using str2
    for char in str2:
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1

    return True


# (d) Compress String Manually (Run-Length Encoding)
def compress_string(text):

    if find_length(text) == 0:
        return ""

    result = ""
    count = 1

    i = 1
    while i <= find_length(text):

        if i < find_length(text) and text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

        i += 1

    return result


# (e) Find Longest Word in Sentence Manually
def find_longest_word(sentence):

    longest = ""
    current_word = ""

    for char in sentence + " ":  # Add space to process last word
        if char != " ":
            current_word += char
        else:
            if find_length(current_word) > find_length(longest):
                longest = current_word
            current_word = ""

    return longest


# ------------------ MAIN PROGRAM ------------------

print("\n=== Customer Support Log Processor ===\n")

log_message = input("Enter support log message: ")
compare_message = input("Enter another message to check anagram: ")

print("\n1. Length of Message:", find_length(log_message))
print("2. Uppercase Version:", convert_to_uppercase(log_message))
print("3. Are Messages Anagrams?:", are_anagrams(log_message, compare_message))
print("4. Compressed Log:", compress_string(log_message))
print("5. Longest Word in Log:", find_longest_word(log_message))