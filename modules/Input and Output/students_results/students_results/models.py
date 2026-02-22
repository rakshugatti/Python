"""
Student model module.
"""

from dataclasses import dataclass, field
from typing import List
from services import GradeCalculator

@dataclass
class Student:
    name: str
    roll_number: str
    marks: List[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        self._validate_marks()

    def _validate_marks(self) -> None:
        if len(self.marks) != 5:
            raise ValueError("Exactly five subject marks are required.")

        for mark in self.marks:
            if not 0 <= mark <= 100:
                raise ValueError("Marks must be between 0 and 100.")

    @property
    def total(self) -> float:
        return sum(self.marks)

    @property
    def percentage(self) -> float:
        return self.total / len(self.marks)

    @property
    def grade(self) -> str:
        return GradeCalculator.calculate(self.percentage)

    def generate_report(self) -> str:
        return (
            f"\n{'='*60}\n"
            f"{'STUDENT RESULT CARD':^60}\n"
            f"{'='*60}\n"
            f"Name        : {self.name}\n"
            f"Roll Number : {self.roll_number}\n"
            f"{'-'*60}\n"
            f"Marks       : {', '.join(f'{m:.2f}' for m in self.marks)}\n"
            f"Total       : {self.total:.2f}\n"
            f"Percentage  : {self.percentage:.2f}%\n"
            f"Grade       : {self.grade}\n"
            f"{'='*60}\n"
        )