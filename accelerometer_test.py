import adafruit_lis3dh
import digitalio
import board
import busio
import time

int1 = digitalio.DigitalInOut(board.GYROSCOPE_INT) # pin connected to interrupt
i2c = busio.I2C(board.GYROSCOPE_SCL, board.GYROSCOPE_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
lis3dh.range = adafruit_lis3dh.RANGE_8_G
for i in range(5):
    print(lis3dh.acceleration)
    time.sleep(5)
