from machine import Pin, I2C, ADC, Timer
from ssd1306 import SSD1306_I2C
from utime import sleep_ms
import gfx
from arduinoMap import mymap 

oled_width = 128
oled_height = 64

# Init Display
i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
oled = SSD1306_I2C(oled_width, oled_height, i2c)
graphics = gfx.GFX(oled_width, oled_height, oled.pixel)

pot = ADC(26)

Y = 65
reading = 0
timer = Timer()

def readAna(timer):
    global Y
    global reading
    reading = pot.read_u16()
    Y = int(mymap(reading, 0, 65535, 62, 12))

timer.init(freq=100, mode=Timer.PERIODIC, callback=readAna)

#oled.invert(True)
graphics.line(0, 10, 126, 10, 1)
graphics.line(0, 63, 126, 63, 1)

while True:
    prevI = 0
    label = 0
    graphics.line(0, 11, 0, 62, 0)
    for i in range(127):
        oled.pixel(i, Y, 1)
        graphics.line(i, Y, i, 61, 1)
        prevI += 1
        if prevI >= 2:
            oled.show()
            prevI = 0
        label = int(mymap(reading, 0, 65535, 0, 101))
        graphics.fill_rect(0, 0, 127, 10, 1)
        if (label < 10):
            xx = int(oled_width/2)-3
        if (label >= 10 and label < 100):
            xx = int(oled_width/2)-8
        elif (label == 100):
            xx = int(oled_width/2)-12
        oled.text('Value:', 3, 1, 0)
        oled.text(str(label), xx, 1, 0)
        graphics.line(i+1, 11, i+1, 62, 0)
        graphics.line(i+2, 11, i+2, 62, 0)
    #oled.fill(0)
    