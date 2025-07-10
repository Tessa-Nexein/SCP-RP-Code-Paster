import sys
import pygetwindow as gw
import keyboard as kb
import time
import pyperclip
from pynput.keyboard import Key, Controller
from pywinauto import Application
import os

# -------------- CONFIG --------------

default_file = "example.txt"        # Change to "clipboard" for clipboard mode
start_hotkey = "f10"              # Hotkey to begin pasting
command_line_key = 'á'            # Command Line key to open SCP:RP's Command Line

# ------------------------------------

keyboard_ctrl = Controller()

def switch_to_roblox():
    try:
        roblox_windows = [w for w in gw.getAllWindows() if 'Roblox' == w.title]
        if roblox_windows:
            hwnd = roblox_windows[0]._hWnd
            app = Application().connect(handle=hwnd)
            app.top_window().set_focus()
            time.sleep(0.2)
            return True
        else:
            print("Roblox window not found.")
            return False
    except Exception as e:
        print(f"Error switching to Roblox: {e}")
        return False

def read_file_lines(filename):
    try:
        with open(f"codes/{filename}", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File not found: codes/{filename}")
        return []

def save_clipboard_to_file():
    content = pyperclip.paste()
    os.makedirs("codes", exist_ok=True)
    with open("codes/clipboard.txt", "w", encoding="utf-8") as f:
        f.write(content)
    return "clipboard.txt"

def type_line(text):
    kb.press(command_line_key)
    kb.release(command_line_key)
    time.sleep(0.05)
    kb.press("backspace")
    kb.release("backspace")

    if text.startswith(":"): text = text[1:]  # Remove leading colon if present

    time.sleep(0.05)
    keyboard_ctrl.type(text)
    time.sleep(0.05)

def wait_for_enter():
    print("Press Enter to send next line...")
    while True:
        if kb.is_pressed("enter"):
            while kb.is_pressed("enter"):
                time.sleep(0.05)
            break
        time.sleep(0.05)

def main():
    print("Roblox Line Paster\n")

    # Check if a command-line argument was passed
    if len(sys.argv) > 1:
        selected = sys.argv[1].strip()
        print(f"Using argument: {selected}")
    else:
        user_input = input(f"Enter filename (or press Enter to use '{default_file}'): ").strip()
        selected = user_input if user_input else default_file

    # Handle clipboard mode
    if selected.lower() == "clipboard":
        print("Clipboard mode selected. Waiting for hotkey...")
        filename = "clipboard.txt"
    else:
        if selected.endswith(".txt"):
            filename = selected
        else:
            filename = f"{selected}.txt"

    print(f"Press {start_hotkey.upper()} to start or ESC to cancel.\n")
    kb.wait(start_hotkey)

    if selected.lower() == "clipboard":
        filename = save_clipboard_to_file()

    lines = read_file_lines(filename)
    if not lines:
        return

    for i, line in enumerate(lines):
        print(f"[{i+1}/{len(lines)}] {line}")
        if not switch_to_roblox():
            break
        type_line(line)
        wait_for_enter()

    print("\nAll lines sent!")


if __name__ == "__main__":
    main()
