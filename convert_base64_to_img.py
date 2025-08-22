import base64
import binascii
from pathlib import Path


def base64_to_image(base64_string: str, save_path: str) -> None:
    """
    Convert Base64 string to image and save to file.

    Args:
        base64_string (str): Base64 encoded string.
        save_path (str): Path to save the decoded image.
    """
    try:
        image_data = base64.b64decode(base64_string, validate=True)
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(image_data)
        print(f"Saved image to: {save_path}")
    except binascii.Error as e:
        print(f"Invalid Base64 string: {e}")


if __name__ == "__main__":
    # Validate a Base64 string
    sample_base64 = "place_the_base64_string_here"

    # Convert Base64 → Image
    base64_to_image(sample_base64, "output/my_image.png")