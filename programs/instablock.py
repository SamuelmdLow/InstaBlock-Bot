import time

import clipboard
import pyautogui
import pretendHuman
import keyboard

blocked_terms = open('blocked_terms.txt', 'r', encoding="utf-8").read().split(",")

def checkBio(bio, blocked_terms):
    found = ''
    for term in blocked_terms:
        if term+" " in bio or " "+term in bio:
            found = found + term + ","

    found = found.replace(" ", "")
    if len(found) > 0:
        found = found[0:-1]
    else:
        found = None

    return found

print("Press space to start!")
while not keyboard.is_pressed("space"):
    pass
print("start!")

for a in range(3):

    filename = 'data.csv'
    file = open(filename, 'a')

    for i in range(5):
        pretendHuman.pretend("checkBio")

        bio = clipboard.paste().lower()
        print("-\n" + bio + "-\n")
        found = checkBio(bio, blocked_terms)
        print(found)
        time.sleep(0.5)

        if found != None:
            print("block")
            pretendHuman.pretend("block")

            file.write("blocked," + found + "\n")

            pyautogui.click(x=699, y=24, button='left')

        else:
            print("good 👍")
            file.write("not blocked\n")

            pyautogui.click(x=699, y=24, button='left')
            pyautogui.press('s')

        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        time.sleep(1)
    file.close()
    pretendHuman.pretend("reload")