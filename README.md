# 📝 SCP:RP Code Paster

A simple Python Script for SCP:RP Roleplayers who need to frequently Morph people or need to paste multi-line codes a lot of times in general

---

## Features

- ✅ Supports **.txt file** or paste straight from **clipboard**
- ✅ Types lines into **SCP:RP's Command Line** with proper timing
- ✅ Manual "Enter to continue" after each line for user control
- ✅ **Command-line support** (run with or without file name parameters)
- ✅ Automatically **focuses the Roblox window** (even if not in focus)
- ✅ Detects and **handles missing files**
- ✅ Automatically **Removes Colums** from the startof the code line

---

## Setup Instructions

1. **Install Python**: [https://python.org](https://python.org)

2. **Download Code Paster**

3. **Folder structure** (create manually if needed):
   ```
   scp-rp-code-paster/
   ├── main.py
   └── codes/
       └── example.txt  # or other text files
   ```


4. **Install dependencies** using the terminal:
   ```bash
   pip install pygetwindow pywinauto keyboard pyperclip pynput requests
   ```

5. **(Optional) Configure the `main.py`**
   
   1) Double Click `main.py` to edit it
   2) Configure the Program as you want in the `OPTIONS` Section
   3) Save by either pressing `CTRL + S` or press `Save` manually

6. **(Optional) Setup up the Shortcuts**

   1) Make a copy of the `example.bat` file
   2) Edit the bat file by `R-Click`ing it then pressing `Edit in Notepad` 
   3) Change `"example.txt"` to any file you want or to `"clipboard"`
   4) Exit and make a Shortcut file for it by `R-Click`ing it then pressing `Show more options` and `Create shortcut`
   5) Move the Shortcut to your Desktop

---

## How to Use

You can run the script in two ways:

### Option 1: Prompt mode
```bash
python main.py
```

- The script will ask for a filename.
- Press **Enter** to use the default (`example.txt`).
- Or type `clipboard` to use what's in your clipboard.
- Or type any filename present in the `/codes` folder

---

### Option 2: With Parameters
```bash
python main.py myfile.txt
```

- Automatically uses `codes/example.txt`
- Skips the prompt and goes straight to hotkey wait

You can also use:
```bash
python main.py clipboard
```
This reads your clipboard and uses it instead of a file.

---

## Hotkey Controls

- **`F10`** = Start pasting lines (can be changed in the code)
- **`Enter`** = Proceed to next line
- **`Esc`** = Exit the program

The script presses the SCP:RP's **Command Line Key** (`á` by default) before typing each line. You can change this key if needed in the script:
```python
command_line_key = 'á'
```

---

## ⚠️ Notes

- Make sure Roblox is **already running** and not minimized.
- If Roblox runs as **Administrator**, you must run this script as Administrator too.
- Lines are typed one at a time, after each, **press Enter** to continue.
- Make sure your `codes/` folder exists or is auto-created.

---

## Customization Tips

- Change `START_HOTKEY` or `COMMAND_LINE_KEY` in the script to match your own setup.
- Enable `AUTO_ENTER` and you will not need to press Enter manually.
- Change `DEFAULT_FILE` to your most commonly used Codes.
- Enable `REPEAT_FOR_CLIPBOARD` if you need to Paste from your Clipboard frequently
- Disable `PRESS_ENTER_MESSAGE` if you are already familiar on how to use the Program. 

