import os
from pynput import keyboard

# Define the log file location
LOG_FILE = "key_log.txt"

print("==================================================")
print("          LOCAL KEYSTROKE RECORDER ENGINE         ")
print("==================================================")
print(f"[*] Recording started. Saving inputs to: {os.path.abspath(LOG_FILE)}")
print("[*] Press the 'ESC' key at any time to exit cleanly.\n")

def on_press(key):
    """Callback function triggered whenever a key is pressed."""
    try:
        # Handle standard alphanumeric keys
        current_key = key.char
    except AttributeError:
        # Handle special/functional keys (e.g., Space, Enter, Backspace)
        if key == keyboard.Key.space:
            current_key = " [SPACE] "
        elif key == keyboard.Key.enter:
            current_key = "\n[ENTER]\n"
        elif key == keyboard.Key.backspace:
            current_key = " [BACKSPACE] "
        else:
            current_key = f" [{str(key).replace('Key.', '').upper()}] "

    # Print to the local terminal for immediate feedback
    print(current_key, end="", flush=True)

    # Append the character to the local log file
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(current_key)

def on_release(key):
    """Callback function triggered whenever a key is released."""
    # Define an exit condition: Stop listener if ESC key is pressed
    if key == keyboard.Key.esc:
        print("\n\n[-] Exit condition met. Stopping recorder engine...")
        return False

# Setup the listener pipeline
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
