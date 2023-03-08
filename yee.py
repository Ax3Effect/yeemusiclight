import yeelight
from yeelight import discover_bulbs, Bulb
import time

from colorama import Fore, Back, Style

brightness_min = 100

ip_address = "192.168.0.100"


class Yee(object):

    cooldown = 0

    def __init__(self):
        self.lamps = []
        self.turned_off = False
        self.lightstrip_only = True
        b = Bulb(ip_address)
        b.turn_on()
        b.set_brightness(100)
        b.start_music()
        self.lamps.append(b)
        '''
        print("Discovering bulbs")
        for bulb in discover_bulbs():
            print("BULB:")
            print(bulb)
            if self.lightstrip_only:
                if bulb["capabilities"]["model"] == "color":
                    continue
            b = Bulb(bulb["ip"])
            print(b)
            b.turn_on()
            b.set_brightness(100)
            b.start_music()
            #b.effect = "sudden"
            self.lamps.append(b)
        '''

    def send_color(self, ra, ga, ba, br):
        self.cooldown = 30

        red = ra * 255
        green = ga * 255
        blue = ba * 255
        if br:
            brightness = min(brightness_min, br * 100)
        else:
            brightness = None
        self.prettyprint(red, green, blue, brightness)
        for b in self.lamps:
            self.turned_off = False
            b.set_rgb(int(red), int(green), int(blue))
            if brightness:
                b.set_brightness(brightness)


    def toggle(self):
        self.cooldown -= 1
        if self.cooldown < 0:
            for b in self.lamps:
                b.set_brightness(1)
                b.set_rgb(1, 1, 1)

    def prettyprint(self, r, g, b, brightness=None):
        if not brightness:
            brightness = 0
        r_space = ""
        g_space = ""
        b_space = ""
        wh_space = ""
        divider = 5
        for i in range(0, int(int(r)/divider)):
            r_space += " "
        for i in range(0, int(int(g)/divider)):
            g_space += " "
        for i in range(0, int(int(b)/divider)):
            b_space += " "
        for i in range(0, int(int(brightness/50))):
            wh_space += " "
        print(Back.RED + str(int(r)) + Back.RED + r_space + Back.GREEN + str(int(g)) + g_space + Back.BLUE + str(int(b)) + b_space + Back.WHITE + str(int(brightness)) + Style.RESET_ALL)