import keyboard
import mouse
import pyautogui

# l x y  | pyautogui.click(x=x, y=y, button='left')
# r x y  | pyautogui.click(x=x, y=y, button='right')
# w text | pyautogui.typewrite('text', interval=0)
# p text | pyautogui.hotkey('ctrl', 'v')
# f text | pyautogui.prompt('function name')

filename = "instructions/" + input("instruction filename: ")+".txt"
file = open(filename, "w")

while keyboard.is_pressed('esc') != True:

    if mouse.is_pressed(button='left'):
        position = mouse.get_position()
        x = position[0]
        y = position[1]

        instruction = "l " + str(x) + " " + str(y) + "\n"
        file.write(instruction)
        print(instruction)

        mouse.wait(button='left', target_types='up')

    elif mouse.is_pressed(button='right'):
        position = mouse.get_position()
        x = position[0]
        y = position[1]

        instruction = "r " + str(x) + " " + str(y) + "\n"
        file.write(instruction)
        print(instruction)

        mouse.wait(button='right', target_types='up')

    elif keyboard.is_pressed("w"):
        text = pyautogui.prompt('text: ').replace(" ", "_")

        instruction = "w " + text + "\n"
        file.write(instruction)
        print(instruction)

    elif keyboard.is_pressed("p"):
        instruction = "p\n"
        file.write(instruction)
        print(instruction)

        while keyboard.is_pressed("p"):
            pass

    elif keyboard.is_pressed("f"):
        function = pyautogui.prompt('function: ')

        instruction = "f " + function + "\n"
        file.write(instruction)
        print(instruction)

file.close()