"""Leap Year utility."""

# Standed Library

# 3rd Party Library

# Project Library


def is_leap_year(year: int):
    """Determine if year is a leap year."""
    if(year % 100 == 0 and (year % 4 != 0 or year % 400 != 0)):
        return False
    elif(year % 4 == 0 or year % 400 == 0):
        return True
    else:
        return False