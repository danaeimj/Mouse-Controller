from pynput.mouse import Button, Controller
from win32api import GetSystemMetrics
import time
from datetime import datetime
from os import system

start_time = time.time()

screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))
screen_center = (GetSystemMetrics(0)/2, GetSystemMetrics(1)/2)
diameter = 20

mouse = Controller()
mouse.position = screen_center
count = 0
while abs(mouse.position[0] - screen_center[0]) < diameter and abs(mouse.position[1] - screen_center[1]) < diameter:
    mouse.click(Button.left, 1)
    now = datetime.now()
    count += 1
    elapsed_t = time.time() - start_time

    elapsed_h = elapsed_t // 3600
    elapsed_m = (elapsed_t % 3600) // 60
    elapsed_s = elapsed_t - elapsed_m*60 - elapsed_h*3600

    print(f"\nCurrent time: {now.hour}:{now.minute}:{now.second}")
    print(f"Elapsed time: {elapsed_h:.0f}:{elapsed_m:.0f}:{elapsed_s:.0f}")
    print(f'Mouse Position: {mouse.position} and mouse clicked {count} times')
    print(f'Code is running...')
    time.sleep(60)

print('Code stopped!')
