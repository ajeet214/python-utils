# pil_tilting_gif.py
from PIL import Image
from pathlib import Path
from typing import Sequence


def create_tilting_gif(
    image_path: str | Path,
    output_path: str | Path,
    tilt_angles: Sequence[int] = (-6, -4, -2, 0, 2, 4, 6, 8),
    padding: tuple[int, int] = (40, 60),
    duration: int = 250
) -> None:
    """
    Creates a GIF that tilts an image around its bottom center.

    Args:
        image_path: Path to the input image (should have transparent background).
        output_path: Path to save the animated GIF.
        tilt_angles: Sequence of angles (degrees) for tilting.
        padding: Extra width and height around image for rotation room.
        duration: Frame duration in milliseconds.
    """
    # Load image
    img = Image.open(image_path).convert('RGBA')

    # Frame size
    frame_width = img.width + padding[0]
    frame_height = img.height + padding[1]
    center = (frame_width // 2, frame_height - padding[1] // 2)

    frames = []

    for angle in tilt_angles:
        # Blank background
        frame = Image.new('RGBA', (frame_width, frame_height), (255, 255, 255, 0))
        # Rotate around bottom center
        rotated = img.rotate(angle, resample=Image.BICUBIC, center=(img.width // 2, img.height))
        # Paste so bottom center aligns
        x = center[0] - img.width // 2
        y = center[1] - img.height
        frame.paste(rotated, (x, y), rotated)
        frames.append(frame)

    # Save GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        disposal=2,
        transparency=0
    )

    print(f"GIF saved as '{output_path}' with size: {frame_width}x{frame_height}")


if __name__ == "__main__":
    create_tilting_gif(
        image_path="../data/images/kibana.png",
        output_path="data/gifs/kibana_tilting_2.gif",
        tilt_angles=(-6, -4, -2, 0, 2, 4, 6, 8),
        padding=(40, 60),
        duration=250
    )
