"""
Description:
A finance-oriented string processing utility that analyzes
transaction descriptions for data normalization and pattern detection.
"""

class FinancialTextAnalyzer:

    def __init__(self, transaction_text: str):
        self.transaction_text = transaction_text

    # (a) Count vowels and consonants
    def count_vowels_consonants(self):
        vowels = "aeiouAEIOU"
        vowel_count = 0
        consonant_count = 0

        for char in self.transaction_text:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

        return vowel_count, consonant_count

    # (b) Reverse string without slicing
    def reverse_text(self):
        reversed_text = ""
        index = len(self.transaction_text) - 1

        while index >= 0:
            reversed_text += self.transaction_text[index]
            index -= 1

        return reversed_text

    # (c) Check palindrome (useful for reference IDs)
    def is_palindrome(self):
        reversed_text = self.reverse_text()
        return self.transaction_text == reversed_text

    # (d) Normalize text to Title Case
    def normalize_title_case(self):
        return self.transaction_text.title()

    # (e) Character frequency analysis
    def character_frequency(self):
        frequency = {}

        for char in self.transaction_text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        return frequency


# ------------------- Main Program -------------------

def main():
    print("\n 🏦Financial Transaction Text Analyzer\n")
    
    transaction_input = input("Enter transaction description or reference ID: ")

    analyzer = FinancialTextAnalyzer(transaction_input)

    vowels, consonants = analyzer.count_vowels_consonants()
    reversed_text = analyzer.reverse_text()
    palindrome_status = analyzer.is_palindrome()
    title_case_text = analyzer.normalize_title_case()
    frequency = analyzer.character_frequency()

    print("\n📊 Analysis Report")
    print("-" * 40)
    print(f"Original Text: {transaction_input}")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Reversed Text: {reversed_text}")
    print(f"Palindrome: {'Yes' if palindrome_status else 'No'}")
    print(f"Normalized (Title Case): {title_case_text}")
    print("\nCharacter Frequency:")

    for key, value in frequency.items():
        print(f"{key} : {value}")


if __name__ == "__main__":
    main()