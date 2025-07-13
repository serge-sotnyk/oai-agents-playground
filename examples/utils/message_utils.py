import base64
from pathlib import Path


def encode_image(image_path: Path) -> str:
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def encode_image_to_data_url(image_path: Path) -> str:
    """
    Encode an image to a data URL format.

    Args:
        image_path: Path to the image file.

    Returns:
        Data URL string of the image.
    """
    encoded_image = encode_image(image_path)
    return f"data:image/png;base64,{encoded_image}"
