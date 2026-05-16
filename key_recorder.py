import os
import sys
import tty
import termios

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
   >> WSL Terminal Event Monitor v2.0 <<
"""

print(BANNER)
print("==================================================")
print(f"[*] Recording started. Saving inputs to: {os.path.abspath(LOG_FILE)}")
print("[*] Exit Hotkey: Press 'Ctrl + X' to safely terminate.")
print("==================================================\n")

def main():
    # Save original terminal settings to restore them later
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
    print("[*] Monitoring active. Start typing below:\n")
    
    try:
        # Switch terminal to raw mode so it catches keys character-by-character
        tty.setraw(sys.stdin.fileno())
        
        while True:
            # Read 1 character from standard input buffer
            char = sys.stdin.read(1)
            
            # Hotkey Detection:
            # '\x18' is Ctrl+X. '\x03' is Ctrl+C.
            if char in ['\x18', '\x03']:
                break
                
            # Format the output visually
            display_key = char
            if char == ' ':
                display_key = " [SPACE] "
            elif char in ['\r', '\n']:
                display_key = "\n[ENTER]\n"
            elif char in ['\x7f', '\x08']:
                display_key = " [BACKSPACE] "
            elif char == '\t':
                display_key = " [TAB] "
                
            # 1. Print immediately to terminal screen
            # (We use sys.stdout because print() behaves differently in raw mode)
            sys.stdout.write(display_key)
            sys.stdout.flush()
            
            # 2. Write and force flush directly to key_log.txt instantly
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(display_key)
                f.flush()
                os.fsync(f.fileno())
                
    finally:
        # CRITICAL: Restore terminal settings back to normal
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print("\n\n[-] Termination hook triggered.")
        print("[*] Session closed cleanly. Data flushed to disk.")

if __name__ == "__main__":
    main()
