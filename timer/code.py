import busio
import board
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_ili9341

try:
    from fourwire import FourWire
except ImportError:
    from displayio import FourWire

# Buzzer setup
buzzer_pin = board.GP0
buzzer =  digitalio.DigitalInOut(buzzer_pin)
buzzer.direction = digitalio.Direction.OUTPUT



# Release any resources currently in use for the displays
displayio.release_displays()

reset = board.GP21

spi = busio.SPI(clock=board.GP18, MOSI=board.GP19, MISO=board.GP20)

# Set up the display bus
cs = board.GP17

dc = board.GP16


display_bus = FourWire(spi, command=dc, chip_select=cs, reset = reset)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

# Set up the display 
splash = displayio.Group()
display.root_group = splash
display.rotation = 1

# Draw a green background
color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(280, 200, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(scale=5, x=57, y=120)
text = ""
minutes_label = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)
splash.append(text_group)

def timer(minutes):
    count = minutes * 60
    for seccond in range(count):
        seconds = count % 60
        print(seconds)
        text_area.text = str(seconds)
        minutes = count / 60
        minutes_label.text
        text_area.text = str(int(minutes)) + " " + str(seconds)
        count -= 1
        time.sleep(1)

# create a function to turn the buzzer on with seconds as a parameter
def buzzer(seconds):
    buzzer.value = True
    time.sleep(seconds)
    buzzer.value = False

timer(44)
while True:
   
    time.sleep(1)
    #buzzer.value = True
    time.sleep(1)
    buzzer.value = False
