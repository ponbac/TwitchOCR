try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

config = '-l eng --oem 1 --psm 3'

print(pytesseract.image_to_string(Image.open('ship.png'), config=config))
