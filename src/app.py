# python -m src.app

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

from src.utils import (get_driver, start_pyautogui, 
                       click_checkbox_on_verification_page, at_target_page)

# from contextlib import contextmanager
# from pathlib import Path

# import pyautogui
# from seleniumbase import Driver



# @contextmanager
# def get_driver(**kwargs):
#     try:
#         driver = Driver(**kwargs)  # undetectable=True, incognito=True
#         yield driver
#     except:
#         print('We had an error!')
#     finally:
#         driver.quit()
#         print('Finished, driver quit.')


# def locate_image_center_on_screen(image_file: str):
#     assert Path(image_file).exists()
#     try: 
#         center = pyautogui.locateCenterOnScreen(image_file, grayscale=True) 
#         return center
#     except:
#         return None


# def click_checkbox_on_verification_page() -> bool:
#     checkbox_image = './images/checkbox.png' 
#     assert Path(checkbox_image).exists()
#     checkbox_center = locate_image_center_on_screen(checkbox_image)
#     if checkbox_center:
#         pyautogui.moveTo(checkbox_center.x, checkbox_center.y, 2, pyautogui.easeInQuad) 
#         pyautogui.click()
#         print('clicked checkbox')
#         sleep(4)  # wait for web page to response
#         pyautogui.moveTo(223, 323, 2, pyautogui.easeInQuad) # move away from the clicked object 
#         pyautogui.click()
#         sleep(4)  # wait for web page to response
#         return True
#     else:
#         return False


# def at_target_page() -> bool:
#     image_on_target_page = './images/email-field-dark.png' # screen partially black out by the cookies setting popup
#     assert Path(image_on_target_page).exists()
#     if locate_image_center_on_screen(image_on_target_page):
#         return True
#     return False


# def start_pyautogui():
#     """start pyautogui 
#     NOTE: if remote interation is not enable yet need to mannually click on popup window to:
#         allow remote interation and 
#         share window
#     """
#     print(f'cursor initial position: {pyautogui.position()}')
#     new_position = (281, 295)  # just a random position to stay out of the way
#     pyautogui.moveTo(*new_position, 2, pyautogui.easeInQuad) 
#     sleep(3)




def run():
    start_pyautogui() 
    with get_driver(undetectable=True, incognito=True) as driver:  
        url = 'https://gitlab.com/users/sign_in'
        driver.uc_open_with_reconnect(url, 10)
        driver.maximize_window()
        sleep(5) # wait long enough for the cloudflare checkbox to appear
        attempt = 0
        while attempt < 3:
            if click_checkbox_on_verification_page():
                if at_target_page():
                    print('bypass verification, at target page!')
                    break
            else:
                print('failed to click checkbox.')
            attempt += 1



if __name__ == '__main__':
    # sleep(15)
    run()

