from face import face

from datetime import datetime
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

from PIL import ImageFont, Image, ImageDraw
import time


class face_message(face):
    def __init__(self, device):
        self._device = device
        self.speed = 0
        self.display_width = 4*8

    def display(self, message):
        message_length = len(message)*6
        for offset in  range(self.display_width, -message_length, -1):
            with canvas(self._device) as draw:
                text(draw, (offset, 1), message, fill="white", font=proportional(LCD_FONT))
            if self.speed:
                time.sleep(1/self.speed)
