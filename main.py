import pyautogui
import time

time_wait_short = 20  # seconds
time_wait_long = 300  # seconds

icon_new = 'images/new.png'
icon_end = 'images/end.png'
icon_alert = 'images/alert.png'
# icon_stop = 'images/stop.png'
icon_stop = 'images/stop2.png'
click_needed = True


def log(message):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f'{now} {message}')


def test(icon):
    print(f'detecting {icon}')
    button_test = pyautogui.locateOnScreen(icon)
    print(button_test)
    if button_test:
        print(f'{icon} in current view')
        # x, y = pyautogui.center(button_test)
        # pyautogui.moveTo(x=x+45, y=y,duration=2)
        # pyautogui.rightClick()
        return True
    print(f'{icon} not in current view')
    return False


def start():
    log("testing for ready")
    if not test(icon_new):
        log("testing failed")
        return
    else:
        test(icon_end)
        log("testing OK")

    while True:
        time.sleep(time_wait_short)

        log("start detecting")
        button = pyautogui.locateOnScreen(icon_alert)
        log("finish detecting with result:")
        print(button)
        if button:
            x, y = pyautogui.center(button)
            log("find the alert window")
            print(f"its center position is ({x}:{y})")
            pyautogui.rightClick(x, y)
            pyautogui.press('enter')
            log("click the button and continue waiting")
            time.sleep(time_wait_long)
        else:
            log("not find the alert window")

        log("start detecting video progress")
        print(f'detecting {icon_stop}')
        button_stop = pyautogui.locateOnScreen(icon_stop)
        if button_stop:
            log("video in stopped status, try to start new video")
            button_new = pyautogui.locateOnScreen(icon_new)
            if button_new:
                log("find new video with result:")
                print(button_new)
                x_new, y_new = pyautogui.center(button_new)
                pyautogui.moveTo(x=x_new + 45, y=y_new, duration=1)
                pyautogui.click()
                log("start playing new video")
            else:
                log("no new videos, bye")
                break
        else:
            log("video is playing")

        if click_needed:
            width, height = pyautogui.size()
            pyautogui.click(width / 2, height / 2)

    log("finished watching video")


if __name__ == '__main__':
    start()
