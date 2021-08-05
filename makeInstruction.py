import keyboard
import mouse
import pyautogui

def unclick(key):
    while keyboard.is_pressed(key):
        pass

# l x y  | pyautogui.click(x=x, y=y, button='left')
# r x y  | pyautogui.click(x=x, y=y, button='right')
# w text | pyautogui.typewrite('text', interval=0)
# p text | pyautogui.hotkey('ctrl', 'v')
# f text | run the function

filename = "programs/instructions/" + input("instruction filename: ")+".txt"
file = open(filename, "w")

print("Press space to create " + filename)
while not keyboard.is_pressed("space"):
    pass
print(filename + " started!")

while keyboard.is_pressed('esc') != True:

    if mouse.is_pressed(button='left'):
        position = mouse.get_position()
        x = position[0]
        y = position[1]

        instruction = "left_click " + str(x) + " " + str(y) + "\n"
        file.write(instruction)
        print(instruction)

        mouse.wait(button='left', target_types='up')

    elif mouse.is_pressed(button='right'):
        position = mouse.get_position()
        x = position[0]
        y = position[1]

        instruction = "right_click " + str(x) + " " + str(y) + "\n"
        file.write(instruction)
        print(instruction)

        mouse.wait(button='right', target_types='up')

    elif keyboard.is_pressed("w"):
        text = pyautogui.prompt('text: ').replace(" ", "_")

        instruction = "write " + text + "\n"
        file.write(instruction)
        print(instruction)

    elif keyboard.is_pressed("p"):
        instruction = "paste\n"
        file.write(instruction)
        print(instruction)

        unclick("p")

    elif keyboard.is_pressed("d"):
        instruction = "delay\n"
        file.write(instruction)
        print(instruction)

        unclick("d")

    elif keyboard.is_pressed("r"):
        instruction = "reload\n"
        file.write(instruction)
        print(instruction)

        unclick("r")

    elif keyboard.is_pressed("down"):
        print("paused")
        unclick("down")
        while not keyboard.is_pressed("down"):
            pass
        unclick("down")
        print("unpaused")

file.close()
print(filename + " finished!")