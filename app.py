# python -m app

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


from time import sleep
from contextlib import contextmanager
from pathlib import Path

import pyautogui
from seleniumbase import Driver


# TODO: verify if screen brightness and contrast setting will affect pyautogui
# TODO: add test for pyautogui

@contextmanager
def get_driver(**kwargs):
    try:
        driver = Driver(**kwargs)  # undetectable=True, incognito=True
        yield driver
    except:
        print('We had an error!')
    finally:
        driver.quit()
        print('Finished, driver quit.')


def click_checkbox() -> bool:
    checkbox_image = './images/checkbox_cf.png' 
    assert Path(checkbox_image).exists()
    try:
        checkbox_center = pyautogui.locateCenterOnScreen(checkbox_image, grayscale=True) 
        pyautogui.moveTo(checkbox_center.x, checkbox_center.y, 3, pyautogui.easeInQuad) 
        pyautogui.click()
        pyautogui.moveTo(223, 323, 3, pyautogui.easeInQuad) # move away from the clicked object 
        pyautogui.click()
        # sleep(2)
        return True
    except:
        return False
    

def is_in_target_page() -> bool:
    target_image = './images/gitlab_email_field.png' 
    assert Path(target_image).exists()

    try:
        if pyautogui.locateCenterOnScreen(target_image, grayscale=True):
            return True
        else:
            return False
    except:
        return False


def start_pyautogui():
    """start pyautogui and enable remote window control"""
    print(f'cursor initial position: {pyautogui.position()}')
    new_position = (281, 295)  # just a random position to stay out of the way
    pyautogui.moveTo(*new_position, 4, pyautogui.easeInQuad) 
    sleep(3)


def run():
    start_pyautogui() 
    with get_driver(undetectable=True, incognito=True) as driver:  
        url = 'https://gitlab.com/users/sign_in'
        driver.uc_open_with_reconnect(url, 10)
        driver.maximize_window()
        sleep(6) # wait long enough for the cloudflare checkbox to appear
        
        attempt = 0
        while attempt < 2:
            if click_checkbox():  # handle cloudflare verification
                print('OK, cloudflare checkbox clicked.')
            else:
                print('Ouch, not able to click checkbox.')
            attempt += 1
            sleep(2)
            if is_in_target_page():
                break

        if is_in_target_page():  # check if is at target home page
            print('OK, at target page.')
        else:
            print('Ouch, something is wrong.')



if __name__ == '__main__':
    run()
