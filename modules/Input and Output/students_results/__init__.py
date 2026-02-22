"""
Student Result Package
Provides models and services for student result processing.
"""

from .models import Student
from .services import GradeCalculator

__all__ = ["Student", "GradeCalculator"]