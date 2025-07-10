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
2. **Install dependencies** using the terminal:
   ```bash
   pip install pygetwindow pywinauto keyboard pyperclip pynput
   ```

3. **Folder structure** (create manually if needed):
   ```
   scp-rp-code-paster/
   ├── main.py
   └── codes/
       └── example.txt  # or other text files
   ```

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
- **`Esc`** = Exit the program  _(Not added yet)_

The script presses the SCP:RP's **Command Line Key** (`á` by default) before typing each line. You can change this key if needed in the script:
```python
command_line_key = 'á'
```

---

## Creating a Shortcut with `.bat`

You can create a `.bat` file to launch it quickly with or without a parameter.

### Example 1: Use Clipboard
```bat
@echo off
cd /d "C:\path\to\your\script"
python main.py clipboard
```

### Example 2: Use Specific File
```bat
@echo off
cd /d "C:\path\to\your\script"
python main.py myscript.txt
```

### Example 3: Prompt-based Start (No Args)
```bat
@echo off
cd /d "C:\path\to\your\script"
python main.py
```

> **Save the above as `start.bat`**, and double-click it to run.

---

## ⚠️ Notes

- Make sure Roblox is **already running** and not minimized.
- If Roblox runs as **Administrator**, you must run this script as Administrator too.
- Lines are typed one at a time — after each, **press Enter** to continue.
- Make sure your `codes/` folder exists or is auto-created.

---

## Customization Tips

- Change `start_hotkey` or `command_line_key` in the script to match your own setup.
- Add more automation like "auto-send after delay" if needed.

---

## 📃 License

