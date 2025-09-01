# Made by: Nexein ☆

import pygetwindow as gw
import keyboard as kb
import time
import pyperclip
from pynput.keyboard import Key, Controller
from pywinauto import Application
import requests

url = "https://raw.githubusercontent.com/Tessa-Nexein/SCP-RP-Morph-Codes/refs/heads/main/commands.json"
response = requests.get(url)
scp_rp_cmd_list = response.json()

banned_args = ["me", "all"]  # Arguments that are not allowed in commands


# --------------- OPTIONS ---------------

auto_enter = False                # If True, Automatically press Enter after each command (Might cause issues with Roblox)
start_hotkey = "f10"              # Hotkey to begin pasting
command_line_key = 'á'            # Command Line key to open SCP:RP's Command Line
display_press_enter = True        # If True, it will display "Press Enter to send next line or Esc to stop..." after each command (Set to false if it bothers you)

# ---------------------------------------

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

def type_command(command):
    kb.press(command_line_key)
    kb.release(command_line_key)
    time.sleep(0.05)
    kb.press("backspace")
    kb.release("backspace")

    time.sleep(0.05)
    keyboard_ctrl.type(command)
    time.sleep(0.05)

def wait_for_enter():
    if display_press_enter or not auto_enter: print("Press Enter to send next line or Esc to stop...\n")

    if auto_enter:
        time.sleep(0.5)
        kb.press("enter")
        kb.release("enter")
        return True
    
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
    if command.strip() == "":
        return False

    if command.startswith(":"):
        command = command[1:]
            
    if command.endswith(",") or command.endswith("&"):
        command = command[:-1]

    if command.split()[0] not in scp_rp_cmd_list:
        print(f"[1;31m# ! > Command '{command.split()[0]}' Command not found in SCP:RP Morphing Commands List. Skipping...\n[0m")
        return False
    
    if command.split(" ")[1] in banned_args:
        print(f"[1;31m# ! > Command '{command}' contains '{command.split()[1]}', which is not allowed. Skipping...\n[0m")
        return False
    
    if command.split[0] == "run":
        print("[1;33m# ! > 'run' Command detected. Skipping... (Not supported)\n[0m")
        return False
    
    return command


def main():
    print("> SCP:RP Line Paster (Morphing Edition) by Nexein☆\n")

    while True:
        print(f"Press {start_hotkey.upper()} to Start Pasting from your Clipboard.\n")
        kb.wait(start_hotkey)
        if not switch_to_roblox():
            print("Failed to switch to Roblox. Exiting.")
            return

        lines_raw = pyperclip.paste().splitlines()
        if not lines:
            return
        lines = [part.strip() 
                for line in lines_raw if line.strip() 
                for part in line.split("&") if part.strip()]

        for i, line in enumerate(lines):
            command = is_valid_command(line)
            if command == False:
                continue

            print(f"[{i+1}/{len(lines)}] {command}")
            if not switch_to_roblox():
                break

            type_command(command)

            if not wait_for_enter():
                print("Program Stopped (Esc pressed).")
                break

        print("Morphing finished!")
        print("\n------------------------------\n")


if __name__ == "__main__":
    main()
