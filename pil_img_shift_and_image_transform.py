from PIL import Image
from pathlib import Path


def shift_image(
    input_path: str | Path,
    output_path: str | Path,
    x_shift: int = 0,
    y_shift: int = 0,
    fill_color: tuple[int, int, int] = (150, 150, 150)
) -> None:
    """
    Shift an image by x and y pixels and fill exposed areas with a color.

    Args:
        input_path: Path to the input image.
        output_path: Path to save the shifted image.
        x_shift: Pixels to shift horizontally (right if positive, left if negative).
        y_shift: Pixels to shift vertically (down if positive, up if negative).
        fill_color: RGB tuple to fill exposed areas.
    """
    # Load image
    im = Image.open(input_path)

    # Apply affine transform
    affine_params = [1, 0, x_shift, 0, 1, y_shift]
    trans_image = im.transform(
        im.size,
        Image.AFFINE,
        affine_params,
        Image.BILINEAR,
        fillcolor=fill_color
    )

    # Save result
    trans_image.save(output_path)
    print(f"Shifted image saved to: {output_path}")


if __name__ == "__main__":
    # Example usage
    shift_image(
        input_path="D:\\test_image.png",
        output_path="D:\\shifted_image.png",
        x_shift=-85,  # shift right 85 pixels
        y_shift=0,
        fill_color=(150, 150, 150)
    )
