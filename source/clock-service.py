import re
import argparse
import time

from datetime import datetime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from PIL import ImageFont

def start_display(n, block_orientation, rotate, inreverse):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
    device.contrast(0)
    return(device)

def display(device):
    number_font = LCD_FONT
    t = datetime.now().time()
    hour = t.strftime("%H")
    minute t.strftime("%M")
    second = t.second

    with  canvas(device) as draw:
        text(draw, (2, 1), hour[0], fill="white", font=number_font)
        text(draw, (8, 1), hour[1], fill="white", font=number_font)
        text(draw, (19, 1), minute[0], fill="white", font=number_font)
        text(draw, (25, 1), minute[1], fill="white", font=number_font)
#        text(draw, (15, 0), ":", fill="white", font=number_font)

#        eights = int(float(second)/60*8)
#        draw.line([(31, 0), (31, eights)], fill="white")
#        draw.line([(0,  0), (0,  eights)], fill="white")
        second_binary = "{0:08b}".format(second)
        for i, value in enumerate(second_binary):
            if value == "1":
                draw.point((15, 7-i), fill="white")
                draw.point((16, 7-i), fill="white")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=4, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=90, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    parser.add_argument('--reverse-order', type=bool, default=True, help='Set to true if blocks are in reverse order')

    args = parser.parse_args()

    try:
        device = start_display(args.cascaded, args.block_orientation, args.rotate, args.reverse_order)
        while True:
            display(device)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
