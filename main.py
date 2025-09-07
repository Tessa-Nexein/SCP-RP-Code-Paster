# Made by: Nexein ☆

import os, sys, time, pyperclip, requests
import pygetwindow as gw
import keyboard as kb
from pynput.keyboard import Key, Controller
from pywinauto import Application

URL = "https://raw.githubusercontent.com/Tessa-Nexein/SCP-RP-Codes/refs/heads/main/commands.json"
try:
    response = requests.get(URL, timeout=5)
    response.raise_for_status()
    scp_rp_cmd_list = response.json()
except Exception as e:
    print(f"Failed to fetch commands list: {e}")
    scp_rp_cmd_list = False

print(scp_rp_cmd_list)


# ----------- OPTIONS -----------

REPEAT_FOR_CLIPBOARD = False      # If True, in clipboard mode, waits for the hotkey and keeps pasting your clipboard until you press Esc
AUTO_ENTER = False                # If True, Automatically press Enter after each command (Might cause issues with Roblox)
DEFAULT_FILE = "example.txt"      # Change to "clipboard" for clipboard mode
START_HOTKEY = "f10"              # Hotkey to begin pasting
COMMAND_LINE_KEY = '`'            # Command Line key to open SCP:RP's Command Line
PRESS_ENTER_MESSAGE = True        # If True, displays a message to press Enter to send the next line
KEY_DELAY = 0.05                  # Delay between key presses (in seconds)

# -------------------------------

keyboard_ctrl = Controller()

def switch_to_roblox():
    try:
        roblox_windows = [w for w in gw.getAllWindows() if "roblox" in w.title.lower()]
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
            return [part.strip() 
                for line in f if line.strip() 
                for part in line.split("&") if part.strip()]
    except FileNotFoundError:
        print(f"File not found: codes/{filename}")
        return []

def save_clipboard_to_file():
    content = pyperclip.paste()
    os.makedirs("codes", exist_ok=True)
    with open("codes/clipboard.txt", "w", encoding="utf-8") as f:
        f.write(content)
    return "clipboard.txt"

def type_command(text):
    kb.press(COMMAND_LINE_KEY)
    kb.release(COMMAND_LINE_KEY)
    time.sleep(KEY_DELAY)
    kb.press("backspace")
    kb.release("backspace")

    if text.startswith(":"): text = text[1:]  # Remove leading colon if present

    time.sleep(KEY_DELAY)
    keyboard_ctrl.type(text)
    time.sleep(KEY_DELAY)

def wait_for_enter():
    if PRESS_ENTER_MESSAGE and not AUTO_ENTER: print("Press Enter to send next line or Esc to stop...\n")
    else: print()  # Just a newline for better readability

    if AUTO_ENTER:
        time.sleep(0.5)
        kb.press("enter")
        kb.release("enter")
        return True # Continue to next line
    
    while True:
        if kb.is_pressed("enter"):
            while kb.is_pressed("enter"):
                time.sleep(0.05)
            return True  # Continue to next line
        if kb.is_pressed("esc"):
            while kb.is_pressed("esc"):
                time.sleep(0.05)
            return False  # Signal to stop
        time.sleep(0.05)

def is_valid_command(command):
    if command == "":
        return False

    # 'While' used in case there are multiple colons at start or multiple commas/semicolons at end
    while command.startswith(":"):
        command = command[1:]

    while command.endswith(","):
        command = command[:-1]
    
    parts = command.split()
    
    if parts[0] == "run":
        print("[1;33m# ! > 'run' Command detected. Skipping... (Not supported)\n[0m")
        return False

    if parts[0] not in scp_rp_cmd_list and scp_rp_cmd_list != False:
        print(f"[1;31m# ! > Command '{parts[0]}' Command not found in SCP:RP Commands List. Skipping...\n[0m")
        return False
    
    return command

def main():
    print("> SCP:RP Line Paster by Nexein☆\n")

    # Check if a command-line argument was passed
    if len(sys.argv) > 1:
        selected = sys.argv[1].strip()
        print(f"Using argument: {selected}")
    else:
        user_input = input(f"Enter filename (or press Enter to use '{DEFAULT_FILE}'): ").strip()
        selected = user_input if user_input else DEFAULT_FILE

    # Handle clipboard mode
    if selected.lower() == "clipboard":
        print("Clipboard mode selected. Waiting for hotkey...")
        filename = "clipboard.txt"
    else:
        if selected.endswith(".txt"):
            filename = selected
        else:
            filename = f"{selected}.txt"

    # Clipboard Mode Loop
    while True:
        stopped = False
        print(f"Press {START_HOTKEY.upper()} to start or ESC to cancel.\n")
        while True:
            if kb.is_pressed(START_HOTKEY):
                while kb.is_pressed(START_HOTKEY):
                    time.sleep(0.05)
                break
            if kb.is_pressed("esc"):
                if not (selected.lower() == "clipboard" and REPEAT_FOR_CLIPBOARD): print("Program Stopped (Esc pressed).")
                else: print("Cycle Cancelled (Esc pressed).")
                return

        if selected.lower() == "clipboard":
            filename = save_clipboard_to_file()

        lines = read_file_lines(filename)
        if not lines:
            print("No lines to process. Restarting Cycle...")
            print("\n------------------------------\n")
            continue

        for i, line in enumerate(lines):
            print(f"[{i+1}/{len(lines)}] {line}")

            if not switch_to_roblox():
                return
            
            if is_valid_command(line): type_command(line)

            if not wait_for_enter():
                stopped = True
                break
        
        if not stopped: print("☑️   All lines sent!")
        elif selected.lower() == "clipboard" and REPEAT_FOR_CLIPBOARD: print("\nCycle Cancelled (Esc pressed).")
        else:
            print("\nPasting Stopped (Esc pressed).")
            return

        print("\n------------------------------\n")

        if not (selected.lower() == "clipboard" and REPEAT_FOR_CLIPBOARD):
            break


if __name__ == "__main__":
    main()
