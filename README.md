# NVIDIA App Color Fixer: Repair Inverted Red & Blue Colors 🛠️

A simple Python script to fix the inverted red/blue color bug caused by the NVIDIA App's high-resolution photo mode.

![Screenshot](https://raw.githubusercontent.com/JohnySir/NVIDIA-SR-Color-Fixer/refs/heads/main/assets/UntitledDiff%20(1).png "Screenshot")

## 🔴 The Issue
There is a known bug triggered by a conflict between recent Windows security updates and the **NVIDIA App**. When using the **Super-Resolution** feature to upscale a capture, the software mistakenly flips the red and blue color channels—saving the final image file in a **BGR** format instead of the standard **RGB** format.

Because most software reads these channels in the standard RGB order, the colors appear inverted:
*   **Warm tones** (orange/red) twist into **Blues**.
*   **Blue tones** (like a blue car or sky) are inverted into a **Rusty Orange**.

## 🚀 What this script does
This script automates the process of swapping those channels back. It:
1.  **Scans** the current folder for image files (`.jpg`, `.jpeg`, `.png`).
2.  **Swaps** the Red and Blue channels back to where they belong.
3.  **Saves** the corrected images into a new folder called `Fixed_Photos` so your originals are never modified.

## 🛠️ How to use (For Beginners)

### 1. Install Python
If you don't have Python installed, download it from [python.org](https://www.python.org/). 
> **Important:** During installation, make sure to check the box that says **"Add Python to PATH"**.

### 2. Setup the Folder
1.  Copy your bugged NVIDIA photos into a folder.
2.  Place `fixer.py` and `requirements.txt` in that same folder.

### 3. Install the Fixer Tool
Open a terminal or Command Prompt in that folder (you can type `cmd` in the address bar of your file explorer) and run:
```bash
pip install -r requirements.txt
```
> **Tip:** Once this command finishes successfully, you can safely delete the `requirements.txt` file to keep your folder clean!

### 4. Run the Fixer
In the same terminal, run:
```bash
python fixer.py
```

### 5. Enjoy your Photos
Check the new `Fixed_Photos` folder that was created. Your images should now look exactly as they did in-game!

## 📦 Requirements
*   **Python 3.x**
*   **OpenCV** (automatically installed via `pip install -r requirements.txt`)

---
*Disclaimer: This is a community workaround script and is not an official fix from NVIDIA or Microsoft.*
