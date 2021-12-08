import board
import time
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from analogio import AnalogIn
import displayio

analog_in = AnalogIn(board.LIGHT)

def get_voltage(pin):
    return (pin.value * 3.3)/65536

display = board.DISPLAY

# Set text, font, and color
text1 = "0000"
text2 = "1111"
text3 = "2222"

font = bitmap_font.load_font("/CMUTypewriter-Regular-70.bdf")
color1 = 0x00AA00
color2 = 0xAAAA00
color3 = 0xAA0000

# Create the tet label
text_area1 = label.Label(font, text=text1, color=color1)
text_area2 = label.Label(font, text=text2, color=color2)
text_area3 = label.Label(font, text=text3, color=color3)

# Set the location
text_area1.x = 10
text_area1.y = 20
text_area2.x = 10
text_area2.y = 90
text_area3.x = 10
text_area3.y = 160


# create group
text_group = displayio.Group()
text_group.append(text_area1)
text_group.append(text_area2)
text_group.append(text_area3)

# Show it
display.show(text_group)



# Loop forever so you can enjoy your text
i = 0
while True:
    light = get_voltage(analog_in)
    text_area1.text = "{0:.6f}".format(light)
    text_area2.text = "{0:.6f}".format(light)
    text_area3.text = "{0:.6f}".format(light)
    time.sleep(0.2)
