from PIL import Image
import requests
from pathlib import Path
from typing import Union

def download_image(url: str, save_path: Union[str, Path]) -> None:
    """
    Downloads an image from a URL and saves it locally.

    Args:
        url (str): The URL of the image.
        save_path (str | Path): Local path to save the image.
    """
    try:
        # Download image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error if status code is not 200

        # Open and save the image
        img = Image.open(response.raw)
        img.save(save_path)

        print(f"Image saved as '{save_path}'")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download image: {e}")
    except IOError as e:
        print(f"Failed to save image: {e}")


if __name__ == "__main__":
    img_url = "https://img.ltwebstatic.com/images3_pi/2023/04/22/1682132328cfa167169f129c340da4fc854d5587b4_thumbnail_600x.jpg"
    download_image(img_url, "cubism.jpg")
