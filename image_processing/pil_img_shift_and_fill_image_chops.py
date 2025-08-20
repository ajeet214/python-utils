from PIL import Image, ImageChops, ImageDraw
from typing import Tuple


def shift_image(
    image_path: str,
    save_path: str,
    x_offset: int = 0,
    y_offset: int = 0,
    fill_color: Tuple[int, int, int] = (150, 150, 150)
) -> None:
    """
    Shifts an image by the specified x and y offsets and fills the exposed areas.

    Args:
        image_path (str): Path to the input image.
        save_path (str): Path to save the shifted image.
        x_offset (int): Pixels to shift horizontally (positive = right, negative = left).
        y_offset (int): Pixels to shift vertically (positive = down, negative = up).
        fill_color (tuple): RGB color to fill exposed areas.
    """
    # Load the image
    im = Image.open(image_path)

    # Shift the image
    shifted = ImageChops.offset(im, xoffset=x_offset, yoffset=y_offset)

    # Draw the exposed area
    draw = ImageDraw.Draw(shifted)
    # Horizontal fill
    if x_offset > 0:
        draw.rectangle((0, 0, x_offset, im.height), fill=fill_color)
    elif x_offset < 0:
        draw.rectangle((im.width + x_offset, 0, im.width, im.height), fill=fill_color)
    # Vertical fill
    if y_offset > 0:
        draw.rectangle((0, 0, im.width, y_offset), fill=fill_color)
    elif y_offset < 0:
        draw.rectangle((0, im.height + y_offset, im.width, im.height), fill=fill_color)

    # Save the result
    shifted.save(save_path)


if __name__ == "__main__":

    shift_image(
        image_path='D:\\test_image.png',
        save_path='D:\\transformed_image.png',
        x_offset=85,        # shift right
        y_offset=0,         # no vertical shift
        fill_color=(150, 150, 150)  # gray fill
    )
