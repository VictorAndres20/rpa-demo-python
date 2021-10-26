# Tests for rpa framework by
# https://rpaframework.org/
import time
from RPA.Desktop import Desktop
from RPA.Excel.Files import Files


def open_firefox():
    desktop = Desktop()
    desktop.move_mouse(desktop.define_region(10, 10, 20, 20))
    desktop.click()
    desktop.move_mouse(desktop.define_region(10, 100, 20, 110))
    desktop.click()

