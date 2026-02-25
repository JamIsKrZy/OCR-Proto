import requests
import base64
from pathlib import Path

TESSERACT_SERVICE = "http://localhost:5000"

def ocr_image(image_path: str, lang: str = "eng", detail: bool = False) -> dict:
    """Send an image to the Tesseract container and get back text."""
    image_bytes = Path(image_path).read_bytes()
    encoded = base64.b64encode(image_bytes).decode("utf-8")

    response = requests.post(
        f"{TESSERACT_SERVICE}/ocr",
        json={
            "image": encoded,
            "lang": lang,
            "detail": detail,
            "config": "--psm 6"  # assume a single block of text
        }
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    result = ocr_image("datasets/invoice/image.jpg")
    print(result["text"])