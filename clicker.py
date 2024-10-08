import threading
from pynput.mouse import Button, Controller
import time

delay = 10  # Time delay between clicks (in seconds)
button = Button.left

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)  # Click the mouse
                time.sleep(self.delay)  # Wait for the delay duration
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

# Start clicking automatically
click_thread.start_clicking()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    click_thread.exit()
