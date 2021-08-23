import pretendHuman
import keyboard
import pyautogui

while True:
    if keyboard.is_pressed("esc"):
        print("pausing")
        while keyboard.is_pressed("esc"):
            pass
        print("done pausing")