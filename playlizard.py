import installLibs
installLibs.install_package("pandas")

from playsound import playsound
import keyboard
import requests

if installLibs.worked == True:
    def playSound():
        playsound('C:/Users/John Neil/Desktop/Python scripts/lizard-button.mp3')
        
    keyboard.add_hotkey('space',playSound)

    keyboard.wait('esc')
    
else:
    print("did not work")