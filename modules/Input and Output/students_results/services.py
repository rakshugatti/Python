"""
Services module for grading logic.
"""


class GradeCalculator:
    """Handles grade calculation."""

    @staticmethod
    def calculate(percentage: float) -> str:
        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 40:
            return "D"
        return "F"