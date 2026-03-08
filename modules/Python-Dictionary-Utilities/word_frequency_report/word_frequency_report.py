# Word Frequency Report Program
# This program reads a paragraph and counts frequency of each word

# Taking paragraph input
paragraph = input("Enter a paragraph:\n")

# Convert text to lowercase to avoid case differences
paragraph = paragraph.lower()

# Split paragraph into words
words = paragraph.split()

# Create empty dictionary for frequency count
word_freq = {}

# Counting frequency of each word
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Display original frequency dictionary
print("\nWord Frequency Dictionary:")
print(word_freq)


# -----------------------------------
# (a) Sort dictionary by keys alphabetically
# -----------------------------------
sorted_by_keys = dict(sorted(word_freq.items()))

print("\nDictionary Sorted by Keys (Alphabetically):")
print(sorted_by_keys)


# -----------------------------------
# (b) Sort dictionary by values in descending order
# -----------------------------------
sorted_by_values = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

print("\nDictionary Sorted by Values (Descending):")
print(sorted_by_values)


# -----------------------------------
# Top 5 most frequent words
# -----------------------------------
print("\nTop 5 Most Frequent Words:")

top5 = list(sorted_by_values.items())[:5]

for word, freq in top5:
    print(word, ":", freq)