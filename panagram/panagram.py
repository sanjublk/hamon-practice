import string


def panagram(s: str) -> bool:
    """Checks if input string is a panagram"""
    letters = set(string.ascii_lowercase)  # made a set containing a to z
    # made a set from input string to checks whether letters is it's subset
    return set(s.lower()) >= letters
