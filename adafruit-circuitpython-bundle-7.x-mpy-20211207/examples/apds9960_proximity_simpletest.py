# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import digitalio
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.I2C()
int_pin = digitalio.DigitalInOut(board.D5)
apds = APDS9960(i2c)

apds.enable_proximity = True
apds.proximity_interrupt_threshold = (0, 175)
apds.enable_proximity_interrupt = True

while True:
    # print the proximity reading when the interrupt pin goes low
    if not int_pin.value:
        print(apds.proximity)

        # clear the interrupt
        apds.clear_interrupt()
