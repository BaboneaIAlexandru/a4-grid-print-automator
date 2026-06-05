# A4 Grid Print Automator

I built this desktop application because my mother was spending too much time manually resizing and copy-pasting images into Word or Paint just to print multiple copies on a single A4 sheet for her job. This script automates the entire process, saving paper and hours of tedious work.

## How to use:
1. Press **`Load new image`** to select a drawing.
2. Select the number of copies (2, 4, or 6) from the dropdown list.
3. Toggle the checkbox to rotate the original image 90° if needed.
4. Check the live preview on the right and press **`Save File`** or **`Print`**.

## Preview

<img width="862" height="648" alt="gui_preview" src="https://github.com/user-attachments/assets/212a459d-ab45-49f5-88be-02df0247503e" />


## How to Run

### Option 1: Download .EXE (Recommended)
Go to the **Releases** section on the right side of this page and download the executable file.

### Option 2: Run from Source
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:
   ```bash
   python gui.py
   ```
