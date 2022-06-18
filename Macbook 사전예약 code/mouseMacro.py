import pyautogui as pa
import os
import time as t

pa.FAILSAFE=False


os.system("explorer https://coupang.com")
t.sleep(0.8)
pa.click(956,219)
t.sleep(0.1)
pa.write("macbook")
t.sleep(0.1)
pa.click(1294, 221)
t.sleep(0.8)
pa.moveTo(680,753)  #쿠팡 맥북 첫번째 상품
pa.click()
t.sleep(1)
pa.click(1085, 628)
t.sleep(0.3)
pa.click(1095, 703)