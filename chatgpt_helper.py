import time
import pyperclip
import pyautogui as pyauto
from vars import *

pyauto.useImageNotFoundException()


def navigate_to_chatgpt():
    try:
        time.sleep(sleep_time)
        pyauto.hotkey(cmd_ctrl, 't')
        time.sleep(sleep_time)
        pyauto.hotkey(cmd_ctrl, 'l')
        time.sleep(gap_time)

        pyauto.write('https://chatgpt.com/')
        time.sleep(gap_time)
        pyauto.hotkey('enter')

        return True

    except pyauto.ImageNotFoundException:
        return False


def type_collect_data(updated_prompt):
    try:

        time.sleep(sleep_time)
        pyperclip.copy(updated_prompt)
        time.sleep(gap_time)
        pyauto.hotkey(cmd_ctrl, 'v')
        time.sleep(sleep_time)

        pyauto.hotkey('enter')
        time.sleep(gap_time)

        for i in range(2):
            pyauto.click(1000, 1000)
            pyauto.hotkey('end')
            time.sleep(sleep_time)

        copy = pyauto.locateOnScreen('copy_chatgpt_button.png', confidence=0.8)
        x_copy = copy.left + (copy.width / 2)
        y_copy = copy.top + (copy.height / 2)
        pyauto.click(x_copy, y_copy)

        collected_profiles = pyperclip.paste()
        collected_profiles = eval(collected_profiles.strip('`').strip('python'))

        time.sleep(gap_time)
        # pyauto.hotkey(cmd_ctrl, 'w')

        return collected_profiles

    except pyauto.ImageNotFoundException:
        return []


def filter_profiles(names, profiles):
    filtered_profiles = {}

    for each_key, each_val in profiles.items():
        if each_val in names:
            filtered_profiles[each_key] = each_val

    return filtered_profiles


def main(names, all_profiles):
    updated_prompt = prompt.format(names)
    navigation_okay = navigate_to_chatgpt()
    if not navigation_okay:
        print("Navigation to chatgpt failed")
        return []

    collected_names = type_collect_data(updated_prompt)
    if not collected_names:
        return []

    filtered_profiles = filter_profiles(collected_names, all_profiles)

    return filtered_profiles
