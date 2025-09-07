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
    print(f"\n[ ERROR ] Failed to fetch commands list: {e}\n")
    scp_rp_cmd_list = False


# ----------- OPTIONS -----------

REPEAT_FOR_CLIPBOARD = True      # If True, in clipboard mode, waits for the hotkey and keeps pasting your clipboard until you press Esc
AUTO_ENTER = False                # If True, Automatically press Enter after each command (Might cause issues with Roblox)
DEFAULT_FILE = "example.txt"      # Change to "clipboard" for clipboard mode
START_HOTKEY = "f10"              # Hotkey to begin pasting
COMMAND_LINE_KEY = 'á'            # Command Line key to open SCP:RP's Command Line
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
            print("[ WARN ] Roblox window not found.\n")
            return False
    except Exception as e:
        print(f"[ ERROR ] Could not switch to Roblox: {e}\n")
        return False

def read_file_lines(filename):
    try:
        with open(f"codes/{filename}", "r", encoding="utf-8") as f:
            return [part.strip() 
                for line in f if line.strip() 
                for part in line.split("&") if part.strip()]
    except FileNotFoundError:
        print(f"[ ERROR ] File not found: codes/{filename}\n")
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

    if text.startswith(":"):
        text = text[1:]  # Remove leading colon if present

    time.sleep(KEY_DELAY)
    keyboard_ctrl.type(text)
    time.sleep(KEY_DELAY)

def wait_for_enter():
    if PRESS_ENTER_MESSAGE and not AUTO_ENTER:
        print("   ↳ Press Enter to send next line, or Esc to stop.\n")
    else:
        print()

    if AUTO_ENTER:
        time.sleep(0.5)
        kb.press("enter")
        kb.release("enter")
        return True
    
    while True:
        if kb.is_pressed("enter"):
            while kb.is_pressed("enter"):
                time.sleep(0.05)
            return True
        if kb.is_pressed("esc"):
            while kb.is_pressed("esc"):
                time.sleep(0.05)
            return False
        time.sleep(0.05)

def is_valid_command(command):
    if command == "":
        return False

    while command.startswith(":"):
        command = command[1:]

    while command.endswith(","):
        command = command[:-1]
    
    parts = command.split()
    
    if parts[0] == "run":
        print("[1;33m[ WARN ] 'run' command detected — Skipping (not supported).\n[0m")
        return False

    if scp_rp_cmd_list:
        if parts[0] not in scp_rp_cmd_list:
            print(f"[1;31m[ ERROR ] Unknown command '{parts[0]}' — Skipping.\n[0m")
            return False
    
    return command

def main():
    print("\n==============================")
    print("   SCP:RP Line Paster")
    print("   Made by: Nexein ☆")
    print("==============================\n")

    if len(sys.argv) > 1:
        selected = sys.argv[1].strip()
        print(f"[ INFO ] Using argument: {selected}\n")
    else:
        user_input = input(f"Enter filename (or press Enter to use '{DEFAULT_FILE}'): ").strip()
        selected = user_input if user_input else DEFAULT_FILE

    if selected.lower() == "clipboard":
        print("[ INFO ] Clipboard mode selected. Waiting for hotkey...\n")
        filename = "clipboard.txt"
    else:
        filename = selected if selected.endswith(".txt") else f"{selected}.txt"

    while True:
        stopped = False
        print(f"[ INFO ] Press {START_HOTKEY.upper()} to start, or Esc to cancel.\n")
        while True:
            if kb.is_pressed(START_HOTKEY):
                while kb.is_pressed(START_HOTKEY):
                    time.sleep(0.05)
                break
            if kb.is_pressed("esc"):
                if not (selected.lower() == "clipboard" and REPEAT_FOR_CLIPBOARD):
                    print("[ INFO ] Program stopped (Esc pressed).\n")
                else:
                    print("[ INFO ] Cycle cancelled (Esc pressed).\n")
                return

        if selected.lower() == "clipboard":
            filename = save_clipboard_to_file()

        lines = read_file_lines(filename)
        if not lines:
            print("[ WARN ] No lines found to process. Restarting...\n")
            print("------------------------------\n")
            continue

        for i, line in enumerate(lines):
            print(f"[ {i+1}/{len(lines)} ] Sending: {line}")

            if not switch_to_roblox():
                return
            
            if is_valid_command(line):
                type_command(line)

            if not wait_for_enter():
                stopped = True
                break
        
        if not stopped:
            print("\n☑️  All lines sent successfully!\n")
        elif selected.lower() == "clipboard" and REPEAT_FOR_CLIPBOARD:
            print("\n[ INFO ] Cycle cancelled (Esc pressed).\n")
        else:
            print("\n[ INFO ] Pasting stopped (Esc pressed).\n")
            return

        print("------------------------------\n")

        if not (selected.lower() == "clipboard" and REPEAT_FOR_CLIPBOARD):
            break


if __name__ == "__main__":
    main()
