import pyautogui
import keyboard
import time

pyautogui.PAUSE = 0

# l x y  | pyautogui.click(x=x, y=y, button='left')
# r x y  | pyautogui.click(x=x, y=y, button='right')
# w text | pyautogui.typewrite('text', interval=0)
# p text | pyautogui.hotkey('ctrl', 'v')
# f text | run the function


def pretend(instructions_filename):
    instructions_location   = "instructions/"+instructions_filename+".txt"
    instructions            = open(instructions_location, "r").readlines()

    for instruction in instructions:

        if keyboard.is_pressed("esc"):
            print("pausing")
            while keyboard.is_pressed("esc"):
                pass

        instruction = instruction.split(" ")
        type = instruction[0]

        if type[-1] == "\n":
            type = type[0:-1]

        if type == "left_click":
            x = int(instruction[1])
            y = int(instruction[2])

            pyautogui.click(x=x, y=y, button='left')

        elif type == "right_click":
            x = int(instruction[1])
            y = int(instruction[2])

            pyautogui.click(x=x, y=y, button='right')

        elif type == "write":
            text = instruction[1].replace("_", " ")

            pyautogui.typewrite(text, interval=0.1)

        elif type == "paste":

            pyautogui.hotkey('ctrl', 'v')
        elif type == "copy":
            x = int(instruction[1])
            y = int(instruction[2])

            pyautogui.dragTo(x, y, button='left', duration=0.1)
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('shift')
            for i in range(9):
                pyautogui.press('down')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('shift')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'c')
        elif type == "find":
            image = instruction[1][0:-1]
            target = pyautogui.locateOnScreen(image)

            if target != None:
                target = pyautogui.center(target)
                x = target[0]
                y = target[1]

                pyautogui.click(x=x, y=y, button='left')

        elif type == "find_adjust":
            image = instruction[1][0:-1]
            time.sleep(0.25)
            target = pyautogui.locateOnScreen(image)
            time.sleep(0.25)
            if target != None:
                target = pyautogui.center(target)
                x = target[0] - 250
                y = target[1] - 10

                pyautogui.click(x=x, y=y, button='right')

        elif type == "reload":

            pyautogui.hotkey('ctrl', 'r')

        elif type == "delay":
            time.sleep(1.5)
        elif type == "delay2":
            time.sleep(0.25)