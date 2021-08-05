import time

import clipboard
import pyautogui
import pretendHuman
import keyboard

curators = ['daily', ' post', 'viral', 'funny', 'memes', 'clips', '|', 'follow ', 'backup', 'hacked', 'dose', 'feed',
            'relatable', 'collab', 'curator', 'admin', 'remov', 'dm', 'inquiries', 'enquiries', 'promo',' ad ', ' ads']
annoying = ['tik', 'tok', 'positivity', 'content', 'creator', 'influencer', 'lifestyle', ' reels', 'goal', 'fan']
count    = ['0k', '1k','2k','3k','4k','5k','6k','7k','8k','9k']
sigma    = ['investor', 'crypto', 'bitcoin', 'business', 'trades', 'entrepreneur', 'study', 'tips']
dislike  = ['📍', '🔞', 'fitness', 'weight lift', 'model', 'exercise', 'language', 'france']

blocked_terms = curators + annoying + count + sigma + dislike

def checkBio(bio, blocked_terms):
    found = ''
    for term in blocked_terms:
        if term in bio:
            found = found + term + ","
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
    for i in range(5):
        pretendHuman.pretend("checkBio")

        bio = clipboard.paste().lower()
        print("-\n" + bio + "-\n")
        found = checkBio(bio, blocked_terms)
        print(found)
        if found != None:
            print("block")
            pretendHuman.pretend("block")
            pyautogui.hotkey('ctrl', 'w')

        else:
            print("good 👍")
            pyautogui.hotkey('ctrl', 'w')
            pyautogui.press('s')

        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        time.sleep(1)

    pretendHuman.pretend("reload")