from PIL import Image
from pathlib import Path
from typing import List, Tuple

def create_pulse_gif(
    icon_path: str | Path,
    save_path: str | Path,
    scales: List[int] = [80, 85, 90, 100, 105, 110, 105, 100, 95, 90, 85],
    frame_padding: Tuple[int, int] = (60, 60),
    frame_duration: int = 250
) -> None:
    """
    Creates a pulsing/zooming animated GIF from a given icon.

    Args:
        icon_path (str | Path): Path to input icon (should support transparency, e.g., PNG).
        save_path (str | Path): Path to save the output GIF.
        scales (List[int], optional): List of scaling percentages for pulse effect. Defaults to standard smooth pulse.
        frame_padding (Tuple[int, int], optional): Extra width & height around the icon for animation space. Defaults to (60, 60).
        frame_duration (int, optional): Duration per frame in milliseconds. Defaults to 250.

    Returns:
        None
    """
    # Load icon
    icon = Image.open(icon_path).convert('RGBA')
    w, h = icon.size

    frame_w, frame_h = w + frame_padding[0], h + frame_padding[1]
    center = (frame_w // 2, frame_h // 2)

    frames: List[Image.Image] = []

    for scale in scales:
        # Resize icon according to current scale
        new_size = (int(w * scale / 100), int(h * scale / 100))
        icon_scaled = icon.resize(new_size, Image.LANCZOS)

        # Create blank frame
        frame = Image.new('RGBA', (frame_w, frame_h), (255, 255, 255, 255))

        # Center the icon in the frame
        x = center[0] - new_size[0] // 2
        y = center[1] - new_size[1] // 2

        frame.paste(icon_scaled, (x, y), icon_scaled)
        frames.append(frame)

    # Save the animated GIF
    frames[0].save(
        save_path,
        save_all=True,
        append_images=frames[1:],
        duration=frame_duration,
        loop=0,
        disposal=2,
        transparency=0
    )

    print(f"Saved GIF: {save_path}")


if __name__ == "__main__":
    # Example usage
    create_pulse_gif(
        icon_path="../data/images/es.png",
        save_path="../data/gifs/es_zoom.gif"
    )
