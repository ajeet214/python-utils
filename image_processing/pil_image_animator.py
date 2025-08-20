# image_animator.py

from PIL import Image
from pathlib import Path
from typing import Sequence, Literal


def animate_icon(
    image_path: str | Path,
    output_path: str | Path,
    animation: Literal["bounce", "tilt", "shake", "slide"] = "bounce",
    duration: int = 300,
    bounce_offsets: Sequence[int] = (0, -8, -15, -18, -15, -8, 0, 5, 0),
    tilt_angles: Sequence[int] = (-6, -4, -2, 0, 2, 4, 6, 8),
    slide_offset: int = 85,
    frame_padding: tuple[int, int] = (40, 60)
) -> None:
    """
    Creates an animated GIF for the given image with different animation effects.

    Args:
        image_path: Path to the input image (supports transparency).
        output_path: Path to save the output GIF.
        animation: Type of animation: "bounce", "tilt", "shake", "slide".
        duration: Frame duration in milliseconds.
        bounce_offsets: Y-offsets for bounce animation.
        tilt_angles: Angles (degrees) for tilt animation.
        slide_offset: Pixel offset for slide animation (to right).
        frame_padding: Extra width and height for tilt animation frames.
    """
    img = Image.open(image_path).convert("RGBA")
    frames = []

    if animation == "bounce":
        w, h = img.size
        frame_size = (w + 20, h + 20)
        center_x = frame_size[0] // 2
        baseline_y = frame_size[1] // 2

        for offset in bounce_offsets:
            frame = Image.new("RGBA", frame_size, (255, 255, 255, 0))
            x = center_x - w // 2
            y = baseline_y - h // 2 + offset
            frame.paste(img, (x, y), img)
            frames.append(frame)

    elif animation == "tilt":
        w, h = img.size
        frame_width = w + frame_padding[0]
        frame_height = h + frame_padding[1]
        center = (frame_width // 2, frame_height - frame_padding[1] // 2)

        for angle in tilt_angles:
            frame = Image.new("RGBA", (frame_width, frame_height), (255, 255, 255, 0))
            rotated = img.rotate(angle, resample=Image.BICUBIC, center=(w // 2, h))
            x = center[0] - w // 2
            y = center[1] - h
            frame.paste(rotated, (x, y), rotated)
            frames.append(frame)

    elif animation == "shake":
        w, h = img.size
        frame_size = (w + 20, h + 20)
        center_x = frame_size[0] // 2
        center_y = frame_size[1] // 2

        shake_offsets = [-5, 5, -4, 4, -2, 2, 0]  # horizontal shake
        for offset in shake_offsets:
            frame = Image.new("RGBA", frame_size, (255, 255, 255, 0))
            x = center_x - w // 2 + offset
            y = center_y - h // 2
            frame.paste(img, (x, y), img)
            frames.append(frame)

    elif animation == "slide":
        w, h = img.size
        frame_size = (w + slide_offset, h)
        for x_offset in range(0, slide_offset + 1, 5):
            frame = Image.new("RGBA", frame_size, (255, 255, 255, 0))
            frame.paste(img, (x_offset, 0), img)
            frames.append(frame)

    else:
        raise ValueError(f"Unknown animation type: {animation}")

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        disposal=2,
        transparency=0
    )
    print(f"Saved {animation} GIF as '{output_path}'")


if __name__ == "__main__":
    # Example usage
    animate_icon(
        "../data/images/kibana.png",
        "data/gifs/kibana_tilting.gif",
        animation="tilt",
        duration=250
    )

    animate_icon(
        "../data/images/Azure OpenAI.png",
        "data/gifs/search_bounce.gif",
        animation="bounce",
        duration=350
    )

    animate_icon(
        "../data/images/Azure OpenAI.png",
        "data/gifs/search_shake.gif",
        animation="shake",
        duration=100
    )

    animate_icon(
        "../data/images/Azure OpenAI.png",
        "data/gifs/search_slide.gif",
        animation="slide",
        duration=50,
        slide_offset=85
    )
