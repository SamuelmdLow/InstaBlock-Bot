import pyautogui
import clipboard

# m x y  | pyautogui.moveTo(x, y, 0)
# l x y  | pyautogui.click(x=x, y=y, button='left')
# r x y  | pyautogui.click(x=x, y=y, button='right')
# p text | clipboard.copy(text) pyautogui.hotkey('ctrl', 'v')

instructions_name   = "instructions.txt"
instructions        = open(instructions_name, "r").readlines()

index = 0
while index < len(instructions):
    instruction = instructions[index].split(" ")

    if instruction[0] == "mt":
        x = int(instruction[1])
        y = int(instruction[2])
        pyautogui.moveTo(x, y, 0)
    elif instruction[0] == "lc":
        x = int(instruction[1])
        y = int(instruction[2])
        pyautogui.click(x=x, y=y, button='left')
    elif instruction[0] == "rc":
        x = int(instruction[1])
        y = int(instruction[2])
        pyautogui.click(x=x, y=y, button='right')
    elif instruction[0] == "pt":
        clipboard.copy(instruction[1])
        pyautogui.hotkey('ctrl', 'v')


    index = index + 1
