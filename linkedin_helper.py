import pyautogui as pyauto
import time
import pyperclip
import re
import bs4
from vars import *

pyauto.useImageNotFoundException()


def fetch_necessary_ul():
    with open("abcd.html", "r", encoding='utf-8') as f:
        data = f.read()

    inilist = [m.start() for m in re.finditer(r'<ul class="display-flex list-style-none flex-wrap">', data)]
    seventh_occ_ind = inilist[0]
    end_list_1 = data[seventh_occ_ind:].find('</ul>')
    end_list = data[end_list_1+seventh_occ_ind+1:].find('</ul>')

    ul_tag = data[seventh_occ_ind:seventh_occ_ind+end_list+end_list_1+5]

    return ul_tag


def fetch_profiles(ul_tag):
    name_urls = {}

    inilist = [(m.start(), m.end()) for m in re.finditer(r'https://www.linkedin.com/in/', ul_tag)]

    for each_val in inilist:
        # finding url
        end_ind = ul_tag[each_val[1]:].find('?')
        url = ul_tag[each_val[0]:each_val[1] + end_ind]

        # finding name
        div_start = ul_tag[each_val[1]:].find('>') + 1
        div_end = ul_tag[div_start:].find('</div>') + 6

        soup = bs4.BeautifulSoup(ul_tag[each_val[1]+div_start:each_val[1]+div_start+div_end])
        name = soup.find('div').text.strip('\n').strip(' ').strip('\n')

        # check and save
        if url not in name_urls:
            name_urls[url] = ''

        name_urls[url] = name

    return name_urls


def fetch_body(link):
    try:
        pyauto.moveTo(1000, 200)
        pyauto.hotkey(cmd_ctrl, 'l')
        pyauto.write(link)
        pyauto.press('left')
        pyauto.press('enter')
        time.sleep(sleep_time)

        for i in range(5):
            pyauto.moveTo(1000, 1000)
            pyauto.hotkey('end')
            time.sleep(sleep_time)

        pyauto.hotkey(cmd_ctrl, shift_opt, 'i')
        time.sleep(10)
        pyauto.click(500, 500)
        time.sleep(sleep_time)

        # finding body tag
        try:
            connect = pyauto.locateOnScreen('body_tag_inspect.png', confidence=0.8)
            x_connect = connect.left + (connect.width / 2) + 500
            y_connect = connect.top + (connect.height / 2)
            pyauto.click(x_connect, y_connect)

        except pyauto.ImageNotFoundException:
                return False

        time.sleep(gap_time)
        pyauto.hotkey(cmd_ctrl, 'c')
        time.sleep(gap_time)
        body_text = pyperclip.paste()

        with open("abcd.html", "w+", encoding="utf-8") as f:
            f.write(body_text)

        time.sleep(gap_time)
        pyauto.hotkey(cmd_ctrl, 'w')

        return True

    except Exception as e:
        print(e)
        return False


def main(link):
    time.sleep(sleep_time)

    body_fetched = fetch_body(link)
    if not body_fetched:
        print("Something went wrong while fetching body")
        return []

    ul_tag = fetch_necessary_ul()
    if not ul_tag:
        print("Something went wrong while fetching ul")
        return []

    linkedin_profiles = fetch_profiles(ul_tag)

    return linkedin_profiles
