import io
from google.cloud import vision


def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Return all the text detected
    try:
        return texts[0].description
    except IndexError:
        return 'no text detected'
