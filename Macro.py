# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 17:16:23 2021

@author: Cris
"""

import time
import pyautogui



bm = 'bm.PNG'
mystic = 'mystic.PNG'
reset = 'reset.PNG'
barman = 'barman.PNG'

i = 0
count_bm = 0
count_mystic = 0
count_rolet = 0

time.sleep(4)

barman_1 = pyautogui.locateOnScreen(barman, confidence=0.7)
bm_1 = pyautogui.locateOnScreen(bm, confidence=0.97)
mystic_1 = pyautogui.locateOnScreen(mystic, confidence=0.97)

# pra garantir que o emulador ficará em primeiro plano
pyautogui.click(barman_1)

time.sleep(0.2)

for i in range(400):
    time.sleep(2.5)
    bm_1 = pyautogui.locateOnScreen(bm, confidence=0.97)
    mystic_1 = pyautogui.locateOnScreen(mystic, confidence=0.98)
    time.sleep(1)
    
    if bm_1 is None and mystic_1 is None:
        
# a tecla "x" está configurada no emulador para scrollar a página
        pyautogui.press("x")
        time.sleep(1.8) 
    bm_1 = pyautogui.locateOnScreen(bm, confidence=0.97)
    mystic_1 = pyautogui.locateOnScreen(mystic, confidence=0.98)
    time.sleep(1)
    
    if bm_1 is None and mystic_1 is None:    
        reset_ok = pyautogui.locateOnScreen(reset, confidence=0.7)
        pyautogui.click(reset_ok)
        pyautogui.click(reset_ok)
        pyautogui.click(reset_ok)
        time.sleep(0.3)
        # a tecla "j" está configurada para confirmar o reset da loja
        pyautogui.press("j")
        pyautogui.press("j")
        pyautogui.press("j")
        count_rolet = count_rolet + 1
        i = i+1
        time.sleep(0.8)

    else:
        time.sleep(0.8)
        
        if bm_1 is not None:
            count_bm = count_bm + 1
            pyautogui.click(bm_1)
        
        if mystic_1 is not None:
            count_mystic = count_mystic + 1
            pyautogui.click(mystic_1)
        
        pyautogui.move(710,15)
        time.sleep(0.5)
        r = pyautogui.position()
        pyautogui.click(r)
        pyautogui.click(r)
        pyautogui.click(r)
        time.sleep(0.5)
        # a tecla "i" está configurada para confirmar alguma compra
        pyautogui.press("i")
        pyautogui.press("i")
        pyautogui.press("i")
        i = i+1

print(count_bm*5)
print(count_mystic*50)
print(count_rolet)

