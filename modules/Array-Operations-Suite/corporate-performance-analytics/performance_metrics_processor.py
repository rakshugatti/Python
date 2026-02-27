"""This module processes monthly performance metrics using
    Python's array module for memory-efficient numeric handling.

    Functionalities:
    - Create array of 10 floating-point metrics
    - Compute total and average performance
    - Determine highest and lowest score manually
    - Reverse array in-place for reverse chronological analysis
"""

from array import array


def process_performance_metrics() -> None:
    """
    Main processing function for performance metrics.
    """

    # Step 1: Create array of 10 floating-point monthly scores
    performance_scores = array('f', [
        78.5, 82.3, 69.4, 91.2, 88.6,
        74.9, 95.1, 80.0, 85.7, 90.4
    ])

    print("Original Monthly Performance Scores:")
    print(performance_scores)

    # Step 2: Calculate total score
    total_score = 0.0
    for score in performance_scores:
        total_score += score

    # Step 3: Calculate average score
    average_score = total_score / len(performance_scores)

    # Step 4: Find maximum and minimum manually
    highest_score = performance_scores[0]
    lowest_score = performance_scores[0]

    for score in performance_scores:
        if score > highest_score:
            highest_score = score

        if score < lowest_score:
            lowest_score = score

    # Step 5: Reverse array in-place
    left = 0
    right = len(performance_scores) - 1

    while left < right:
        performance_scores[left], performance_scores[right] = \
            performance_scores[right], performance_scores[left]

        left += 1
        right -= 1

    # Display computed results
    print("\nTotal Performance Score:", round(total_score, 2))
    print("Average Performance Score:", round(average_score, 2))
    print("Highest Score:", highest_score)
    print("Lowest Score:", lowest_score)

    print("\nReversed Scores (Latest to Oldest View):")
    print(performance_scores)


if __name__ == "__main__":
    process_performance_metrics()