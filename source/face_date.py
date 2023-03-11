from face import face

from datetime import datetime
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

from PIL import ImageFont
import time

class face_date(face):
    def __init__(self, device):
        self._font = proportional(TINY_FONT)
        self._device = device

    def display(self):
        t = datetime.now()
        year = t.strftime("%Y")
        month = t.strftime("%m")
        weekday = t.strftime("%a")
        day = t.strftime("%d")

        with  canvas(self._device) as draw:
            text(draw, (0, -1), day, fill="white", font=self._font)
            text(draw, (8, 0), month, fill="white", font=self._font)
            text(draw, (17,1), year, fill="white", font=self._font)
            time.sleep(1)
