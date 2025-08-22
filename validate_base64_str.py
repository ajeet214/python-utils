import re


def is_base64(s: str) -> bool:
    """
    Validate if a string is valid Base64.
    
    Args:
        s (str): String to validate.
    
    Returns:
        bool: True if valid Base64, False otherwise.
    """
    expression = r"^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$"
    return bool(re.fullmatch(expression, s))


if __name__ == "__main__":
    # Validate a Base64 string
    sample_base64 = "place_the_base64_string_here"
    print("Base64 validation:", "Valid" if is_base64(sample_base64) else "Invalid")