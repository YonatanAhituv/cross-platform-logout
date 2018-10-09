from time import sleep

 
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import audioio
import board
import digitalio

mac = False
windows = False
chrome = False

# enable the speaker
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

# make the 2 input buttons
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN
 
buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

def play(file):
    f = open(file, "rb")
    wav = audioio.WaveFile(f)
    a = audioio.AudioOut(board.A0)
    a.play(wav)


while True:
    if buttonA.value:
        sleep(0.1)
        if buttonB.value:
            print("mac")
            mac = True
        else:
            print("chromeos")
            chrome = True
        break
    if buttonB.value:
        sleep(0.1)
        if buttonA.value:
            print("mac")
            mac = True
        else:
            print("windows")
            windows = True
        break

if mac:
    leftCtrl = Keycode.LEFT_GUI
else:
    leftCtrl =  Keycode.LEFT_CONTROL

sleep(1)
keyboard = Keyboard()
layout = KeyboardLayoutUS(keyboard)
sleep(0.500)
if windows:
    keyboard.press(Keycode.LEFT_GUI, Keycode.R)
    sleep(0.01)
    keyboard.release_all()
    sleep(0.200)
    layout.write("cmd\n")
    sleep(0.100)
elif mac:
    keyboard.press(Keycode.LEFT_GUI)
    layout.write(" ")
    sleep(0.1)
    keyboard.release_all()
    layout.write("terminal")
    sleep(0.5)
    keyboard.press(Keycode.RETURN)
    sleep(0.1)
    keyboard.release_all()
    sleep(0.5)
else:
    keyboard.press(leftCtrl)
    layout.write("t")
    sleep(0.1)
    keyboard.release_all()
play("alarm.wav")
if windows:
    layout.write("color a\n")
layout.write("WARNING ")
sleep(0.1)
layout.write("WARNING ")
sleep(0.400)
layout.write("MALWARE DETECTED!!! ")
sleep(0.200)
layout.write("COMPUTER ")
sleep(0.100)
layout.write("WILL ")
sleep(0.100)
layout.write("SELF ")
sleep(0.100)
layout.write("DESTRUCT ")
sleep(0.100)
layout.write("IN: ")
sleep(0.100)
layout.write("5")
sleep(1.000)
layout.write(" 4 ")
sleep(1.000)
layout.write("3 ")
sleep(1.000)
layout.write("2 ")
sleep(1.000)
layout.write("1 ")
sleep(1.000)
layout.write("BOOOM")

if chrome or mac:
    keyboard.press(leftCtrl, Keycode.SHIFT)
    keyboard.press(Keycode.Q)
    keyboard.release_all()
    sleep(0.1)
    keyboard.press(leftCtrl, Keycode.SHIFT)
    keyboard.press(Keycode.Q)
    sleep(0.1)
    keyboard.release_all()
elif windows:
    keyboard.press(leftCtrl, Keycode.LEFT_ALT)
    sleep(0.100)
    keyboard.press(Keycode.DELETE)
    sleep(0.100)
    keyboard.release_all()
    sleep(0.200)
    keyboard.press(Keycode.TAB)
    sleep(0.05)
    keyboard.release_all()
    sleep(0.05)
    keyboard.press(Keycode.TAB)
    sleep(0.05)
    keyboard.release_all()
    sleep(0.100)
if windows or mac:
    keyboard.press(Keycode.RETURN)
    sleep(0.05)
    keyboard.release_all()