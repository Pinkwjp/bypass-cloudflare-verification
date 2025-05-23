

# NOTE: when encounter 'Xlib.error.DisplayConnectionError'
# in Linux terminal run: 'xhost +' 
# response: 'access control disabled, clients can connect from any host'

# NOTE: not able to handld cloudflare with builtin seleniumbase methods

# NOTE: not able to locate cloudflare iframe with driver.find_element

# NOTE: on Fedora, need Python 3.10 to be compatible with pyautogui and its dependencies

# NOTE: seems like pyautogui.locateCenterOnScreen prefer simple image with simple lines

# NOTE: As of pyautogui version 0.9.41, if the locate functions can’t find the provided image, 
# they’ll raise ImageNotFoundException instead of returning None.

# NOTE:
# with SB(undetected=True, incognito=True) as driver:
# with DriverContext(uc=True) as driver: 
# both these context managers seem not fully compatible with Fedora, 
# causing error: "X11 display failed! Will use regular xvfb!"

# NOTE: on Fedora, need the followings libs for pyautogui
# sudo dnf install scrot
# sudo dnf install python3-tkinter
# sudo dnf install python3-devel

# use pipenv to generate requirements.txt 
# pipenv run pip freeze > requirements.txt       
# pipenv requirements > requirements.txt 





from time import sleep

from src.utils import (get_driver, start_pyautogui, 
                       handle_verification)


def run():
    start_pyautogui() 
    with get_driver(undetectable=True, incognito=True) as driver:  
        url = 'https://gitlab.com/users/sign_in'
        driver.uc_open_with_reconnect(url, 10)
        sleep(2)
        driver.maximize_window()
        sleep(5) # wait long enough for the cloudflare checkbox to appear
        if handle_verification():
            print('bypass cloudflare verification!')
        else:
            print('failed to click checkbox.')



if __name__ == '__main__':
    # python -m app

    # sleep(10)
    run()

