from collections import Counter

# Example 1: Election Vote Counting
def vote_counter():
    votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

    result = Counter(votes)

    print("\nVote Results:")
    print(result)


# Example 2: Password Character Analysis
def character_counter():
    password = "securepassword123"

    char_count = Counter(password)

    print("\nCharacter Frequency:")
    print(char_count)