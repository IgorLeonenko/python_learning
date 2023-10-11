import pyautogui
import pyscreeze
import PIL
import time

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

def detect_obstacle(screenshot, x, y_range):
  for y in y_range:
    if screenshot.getpixel((x, y)) < (100, 100, 100):
      return True
  return False


while True:
  screenshot = pyautogui.screenshot()

  if detect_obstacle(screenshot, 300, range(0, 1500)):
    pyautogui.press('space')
  elif detect_obstacle(screenshot, 300, range(400, 440)):
    pyautogui.press('down')

  time.sleep(0.01)
