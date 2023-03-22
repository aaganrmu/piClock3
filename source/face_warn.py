from face import face

from datetime import datetime
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

import time

class face_warn(face):
    def __init__(self, device):
        self._device = device
        self.flashes = 10
        self.length = 0.5

    def display(self, message):
        for i in range(self.flashes):
            with canvas(self._device) as draw:
                text(draw, (0, 1), message, fill="white", font=proportional(LCD_FONT))
            time.sleep(self.length/2)
            with canvas(self._device) as draw:
                draw.rectangle(((0,0),(8*4-1,7)), fill="white")
                text(draw, (0, 1), message, fill="black", font=proportional(LCD_FONT))
            time.sleep(self.length/2)