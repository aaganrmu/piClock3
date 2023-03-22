from face import face

from datetime import datetime
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

from PIL import ImageFont
import time

class face_time(face):
    def __init__(self, device):
        self._font = LCD_FONT
        self._device = device

    def display(self):
        t = datetime.now().time()
        hour = t.strftime("%H")
        minute = t.strftime("%M")
        second = t.second

        with canvas(self._device) as draw:
            text(draw, (2, 1), hour[0], fill="white", font=self._font)
            text(draw, (8, 1), hour[1], fill="white", font=self._font)
            text(draw, (19, 1), minute[0], fill="white", font=self._font)
            text(draw, (25, 1), minute[1], fill="white", font=self._font)

            second_binary = "{0:08b}".format(second)
            for i, value in enumerate(second_binary):
                if value == "1":
                    draw.point((15, i), fill="white")
                    draw.point((16, i), fill="white")
        time.sleep(1)
