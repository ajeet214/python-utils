# pil_bounce_icon_gif.py
from PIL import Image
from pathlib import Path
from typing import Sequence, Tuple


def create_bounce_gif(
    icon_path: str | Path,
    output_path: str | Path,
    bounce_offsets: Sequence[int] = (0, -8, -15, -18, -15, -8, 0, 5, 0),
    frame_padding: int = 30,
    duration: int = 350,
) -> None:
    """
    Creates a bouncy GIF animation of an icon.

    Args:
        icon_path: Path to the icon image (should support transparency).
        output_path: Path to save the animated GIF.
        bounce_offsets: Sequence of vertical offsets to simulate bounce.
        frame_padding: Extra space around the icon for movement.
        duration: Duration of each frame in milliseconds.
    """
    icon = Image.open(icon_path).convert('RGBA')
    w, h = icon.size

    frame_size = (w + 2 * frame_padding, h + 2 * frame_padding)
    center_x = frame_size[0] // 2
    baseline_y = frame_size[1] // 2

    frames = []

    for offset in bounce_offsets:
        frame = Image.new('RGBA', frame_size, (255, 255, 255, 0))
        x = center_x - w // 2
        y = baseline_y - h // 2 + offset
        frame.paste(icon, (x, y), icon)
        frames.append(frame)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        disposal=2,
        transparency=0
    )

    print(f"Saved: {output_path}")


if __name__ == "__main__":
    create_bounce_gif(
        icon_path="../data/images/Azure OpenAI.png",
        output_path="../data/gifs/search_bounce.gif",
        bounce_offsets=(0, -8, -15, -18, -15, -8, 0, 5, 0),
        frame_padding=30,
        duration=350
    )
