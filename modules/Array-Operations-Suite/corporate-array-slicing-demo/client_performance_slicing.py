""" array slicing techniques using Python's array module.

    Operations:
    - Extract sub-array
    - Reverse using slicing
    - Copy array
    - Step slicing with custom interval
"""

from array import array


def main():

    # Step 1: Create weekly client satisfaction scores
    weekly_scores = array('i', [78, 82, 85, 90, 88, 76, 95, 89, 84, 92])

    print("Original Weekly Scores:")
    print(weekly_scores)

    # (a) Extract sub-array (Weeks 3 to 6)
    sub_array = weekly_scores[2:6]
    print("\nSub-array (Weeks 3 to 6):")
    print(sub_array)

    # (b) Reverse using slicing
    reversed_array = weekly_scores[::-1]
    print("\nReversed Array (Latest to Oldest):")
    print(reversed_array)

    # (c) Copy array
    copied_array = weekly_scores[:]
    print("\nCopied Array (Backup Data):")
    print(copied_array)

    # (d) Step slicing (Analyze alternate weeks)
    alternate_weeks = weekly_scores[::2]
    print("\nAlternate Week Scores (Step = 2):")
    print(alternate_weeks)


if __name__ == "__main__":
    main()