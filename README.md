# 📝 SCP:RP Code Paster - Morphing Version

A simple Python Script for SCP:RP Morphers to Morph Roleplayers with easy and safety

---

## Features

- ✅ Pastes Morphs straight from your **Clipboard**
- ✅ Types lines into **SCP:RP's Command Line** with proper timing
- ✅ Manual **"Enter to continue"**, or optional **Auto-Enter** after each line
- ✅ Automatically **focuses the Roblox window** (even if not in focus)
- ✅ Automatically **Removes Colums** from the startof the code line
- ✅ Detects and **handles Banned commands**
- ✅ **Excludes Non-Command lines** (eg.: Empty lines, Random texts)

---

## Setup Instructions

1. **Install Python**: [https://python.org](https://python.org)

2. **Download Code Paster**

3. **Install dependencies** using the terminal:
   ```bash
   pip install pygetwindow pywinauto keyboard pyperclip pynput requests
   ```

4. **(Optional) Configure the `main.py`**
   
   1) Double Click `main.py` to edit it
   2) Configure the Program as you want in the `OPTIONS` Section
   3) Save by either pressing `CTRL + S` or press `Save` manually

5. **Move the already provided `Shortcut` file to your Desktop**

6. **Start the Code Paster with the Shortcut**

---

## How to Use

1. **Start Code Paster with the Shortcut**

2. **Copy the `Morph` you want to Paste**

3. **Press the Start Hotkey button (`F10` by default)**

4. **Press `Enter` after Code Paster has Pasted the line into Command Bar**

5. **Repeat. No need to Restart the program.**

---

## Hotkey Controls

- **`F10`** = Start pasting lines (can be changed in the code)
- **`Enter`** = Proceed to next line
- **`Esc`** = Exit the program

The script presses the SCP:RP's **Command Line Key** ( ` by default) before typing each line. You can change this key if needed in the script:
```python
command_line_key = '`'
```

---

## ⚠️ Notes

- Make sure Roblox is **already running** and not minimized.
- If Roblox runs as **Administrator**, you must run this script as Administrator too.
- Lines are typed one at a time — after each, **press Enter** to continue.

---

## Customization Tips

- Change `start_hotkey` or `command_line_key` in the script to match your own setup.
- Add or remove `banned_args` at the top of the script

