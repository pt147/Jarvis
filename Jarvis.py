import os
import pyautogui
import time


def mount_disk():
    os.system('rm dump.dat')
    os.system('lsblk | grep sd | cut -f1-2 -d" "> dump.dat')

    with open('dump.dat', 'r') as f:
        for data in f:
            # convert data to list->l
            l = list(data)

            # remove non-ascii chars from list l [1-3]
            l[:2] = ""

            # echo to screen. now remove what we don't need.
            # print(l[4:8])

            # now convert to standard string.
            dev = l[:4]

            device = ""

            for char in dev:
                device += char
            print(device)
            # plug string to terminal commands ( create dir's to mount)
            if device == 'sda3':
                os.system('cd .. && cd .. && cd .. && cd /media/nir/ && echo admin123|sudo -S mkdir DATA-D')
                # mount each device to each dir.
                os.system('echo admin123 | sudo -S mount /dev/sda3 /media/nir/DATA-D')
            elif device == 'sda4':
                os.system('cd .. && cd .. && cd .. && cd /media/nir/ && echo admin123|sudo -S mkdir DATA-E')
                # mount each device to each dir.
                os.system('echo admin123 | sudo -S mount /dev/sda4 /media/nir/DATA-E')

    pyautogui.sleep(10)

    # if checkIfScreenOpen():
    openAndroidStudio()
    openChrome()


def openAndroidStudio():
    pyautogui.click(31, 201)


def checkIfScreenOpen():
    while True:
        if pyautogui.locateOnScreen('screen_from_python.png') is not None:
        # pyautogui.alert('Your computer is Ready to go Master..')
            break

    return True


def openChrome():
    pyautogui.click(32, 65)
    pyautogui.sleep(30)
    pyautogui.typewrite('http://192.168.1.2:8090/')
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.press('tab')
    pyautogui.typewrite('Parth Thakar')
    pyautogui.press('tab')
    pyautogui.typewrite('1234')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.click(31, 201)
    pyautogui.sleep(2)
    pyautogui.alert('Your computer is Ready to go Master..')


# mount_disk()


# pyautogui.sleep(2)
# myScreenshot = pyautogui.screenshot(region=(400,100, 100, 100))
# myScreenshot.save('screen_from_python.png')
# print(pyautogui.locateOnScreen('screen_from_python.png'))


mount_disk()
