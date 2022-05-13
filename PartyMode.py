import pyautogui
from pynput.keyboard import Listener, KeyCode
import time
import threading
from pynput.mouse import Button, Controller
import random
import keyboard

delay: float = 0.000000000000000001
start_stop_key: KeyCode = KeyCode(char='`')
exit_key: KeyCode = KeyCode(char='1')
letters_per_entry: int = 100

def button() -> str:
    return random.choice(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"])

class ClickMouse(threading.Thread):
    def __init__(self, delay):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True
        self.total_letters = 0

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        print(f"PARTYMODE ENABLED 🎊🎊🎊\nDelay: {delay}\nLetters per entry: {letters_per_entry}\nPress {start_stop_key} to start/stop it.\nPress {exit_key} to exit PartyMode.")
        while self.program_running:
            while self.running:
                keyboard.write("".join(button() for _ in range(letters_per_entry)), delay=self.delay)
                self.total_letters += 1
            time.sleep(self.delay)
        print(f"AWWWWWWW PARTYMODE SHUTTING DOWN\nLetters spammed: {self.total_letters}")


mouse = Controller()
click_thread = ClickMouse(delay)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
