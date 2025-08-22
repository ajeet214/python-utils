import base64


def image_to_base64(image_path: str) -> str:
    """
    Convert an image file to a Base64 encoded string.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Base64 encoded string.
    """
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return encoded


if __name__ == "__main__":

    # Convert Image → Base64
    b64_str = image_to_base64("sample.png")
    print("Encoded Base64 string:", b64_str[:100], "...")  # print only first 100 chars