import PIL.ImageGrab
from datetime import datetime


def take_screenshot():
    image = PIL.ImageGrab.grab(bbox=(0, 660, 600, 910))
    # print(image.getbbox())
    # image.show()

    path = 'images/' + str(datetime.now())[:-7].replace(':', '-') + '.png'
    image.save(path, 'PNG')

    return path


take_screenshot()
