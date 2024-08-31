import pyautogui as pyauto
import time
from vars import *

pyauto.useImageNotFoundException()


def navigate_to_profile(profile_link):
    pyauto.moveTo(1000, 200)
    pyauto.hotkey(cmd_ctrl, 'l')
    pyauto.write(profile_link)
    pyauto.press('enter')


def more_connect():
    try:
        more = pyauto.locateOnScreen('more_button.png', confidence=0.8)
        x_more = more.left + (more.width / 2)
        y_more = more.top + (more.height / 2)
        pyauto.click(x_more, y_more)

        connect = pyauto.locateOnScreen('connect_more_button.png', confidence=0.8)
        x_connect = connect.left + (connect.width / 2)
        y_connect = connect.top + (connect.height / 2)
        pyauto.click(x_connect, y_connect)

        return True

    except pyauto.ImageNotFoundException:
        return False


def send_request(message):
    time.sleep(sleep_time)

    # going to connect
    try:
        connect = pyauto.locateOnScreen('connect_button.png', confidence=0.8)
        x_connect = connect.left + (connect.width / 2)
        y_connect = connect.top + (connect.height / 2)
        pyauto.click(x_connect, y_connect)

    except pyauto.ImageNotFoundException:
        if not more_connect():
            return False

    time.sleep(gap_time)

    # adding note
    try:
        add_note = pyauto.locateOnScreen('add_note_button.png', confidence=0.8)
        x_add_note = add_note.left + (add_note.width / 2)
        y_add_note = add_note.top + (add_note.height / 2)
        pyauto.click(x_add_note, y_add_note)

    except pyauto.ImageNotFoundException:
        return False

    time.sleep(gap_time)
    pyauto.write(message)
    time.sleep(gap_time)

    # sending request
    try:
        add_note = pyauto.locateOnScreen('send_button.png', confidence=0.8)
        x_add_note = add_note.left + (add_note.width / 2)
        y_add_note = add_note.top + (add_note.height / 2)
        pyauto.click(x_add_note, y_add_note)

    except pyauto.ImageNotFoundException:
        return False

    return True


def main(dict_of_profiles, role, company_name):
    i = 0
    for each_profile, each_name in dict_of_profiles.items():
        if i > 1:
            break
        i += 1

        navigate_to_profile(each_profile)

        formatted_message = message.format(each_name, role, company_name)

        request_sent = send_request(formatted_message)
        if request_sent:
            print(f"Request sent to {each_profile}")
        else:
            print("Something broke")

        time.sleep(sleep_time)

    pyauto.hotkey(cmd_ctrl, 'w')

    return True
