# A4 Grid Print Automator

I built this desktop application because my mother was spending too much time manually resizing and copy-pasting images into Word or Paint just to print multiple copies on a single A4 sheet for her job. This script automates the entire process, saving paper and hours of tedious work.

## How to use:
1. Press **`Load new image`** to select an image.
2. Select the number of copies (2, 4, 6, or 8) from the dropdown list.
3. Toggle the checkbox to rotate the original image 90° if needed.
4. Enable **`Grayscale`** if you want to save color ink or print in black and white.
5. Enable **`Show cut guidelines`** to draw helper grid lines for precise paper cutting.
6. Check the live preview on the right and press **`Save File`** or **`Print`**.

## Preview

| Dark Mode | Light Mode |
| :---: | :---: |
| <img width="859" height="647" alt="GUI preview v1 1 0 (dark mode) (1)" src="https://github.com/user-attachments/assets/f6cf1996-068e-44a2-8729-2a200ba2f0d4" /> | <img width="862" height="649" alt="GUI preview v1 1 0 (light mode)" src="https://github.com/user-attachments/assets/7b2c29ba-183b-40a9-942b-8122d4437df3" /> |

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
