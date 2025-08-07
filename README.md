# Caesar Cipher GUI

## Overview
The Caesar Cipher GUI is a Python application that provides a graphical interface for encrypting and decrypting text using the Caesar Cipher algorithm. Built with Tkinter, it allows users to input a message, specify a shift value, choose between encryption and decryption, and view the result in a user-friendly window.

## Features
- **Graphical Interface**: Clean, modern UI with input fields, radio buttons, and buttons for processing, clearing, and exiting.
- **Encryption/Decryption**: Supports both operations with any integer shift value (normalized to 0-25).
- **Input Validation**: Prevents empty messages and non-numeric shift values, with visual feedback (red-tinted fields) and error pop-ups.
- **Styling**: Uses `ttk` widgets, Helvetica fonts, and a light gray background for a polished look.
- **Error Handling**: Handles invalid inputs and keyboard interrupts gracefully.
- **Window Management**: Centered, non-resizable window (400x350 pixels).

## Requirements
- **Python**: Version 3.x.
- **Tkinter**: Included with standard Python on Windows/macOS; install with `sudo apt-get install python3-tk` on Debian/Ubuntu or `sudo dnf install python3-tkinter` on Fedora.
- **Graphical Environment**: Windows, macOS, or Linux with a display server (X11/Wayland). For headless servers, use X11 forwarding (`ssh -X`) or a virtual display (`xvfb-run`).

## Installation
1. Ensure Python 3 is installed:
   ```bash
   python3 --version
   ```
2. Verify Tkinter is installed:
   ```bash
   python3 -c "import tkinter; print(tkinter.TkVersion)"
   ```
   If not installed, install it (e.g., `sudo apt-get install python3-tk` on Ubuntu).
3. Download the `caesar_cipher_gui.py` script.
4. (Optional) For headless servers:
   - Install `Xvfb`: `sudo apt-get install xvfb`.
   - Run with: `xvfb-run python3 caesar_cipher_gui.py`.

## Usage
1. Run the script:
   ```bash
   python3 caesar_cipher_gui.py
   ```
2. In the GUI:
   - Enter a message in the "Message" field.
   - Enter a shift value (any integer) in the "Shift Value" field.
   - Select "Encrypt" or "Decrypt" via radio buttons.
   - Click "Process" to see the result in the text area.
   - Click "Clear" to reset inputs or "Exit" to close the application.
3. Error Handling:
   - Empty messages or non-numeric shift values trigger error messages and highlight the invalid field in red.
   - Press Ctrl+C to exit gracefully (prints "Goodbye!" in the terminal).

## Example
- **Input**: Message = "Hello", Shift = 3, Mode = Encrypt
- **Output**: Encrypted message = "Khoor"
- **Input**: Message = "Khoor", Shift = 3, Mode = Decrypt
- **Output**: Decrypted message = "Hello"

## Troubleshooting
- **Error: `_tkinter.TclError: no display name and no $DISPLAY environment variable`**:
  - Run on a system with a GUI (Windows, macOS, or Linux with X11/Wayland).
  - For remote servers, enable X11 forwarding: `ssh -X user@remote_host`.
  - For headless servers, use: `xvfb-run python3 caesar_cipher_gui.py`.
  - Check `DISPLAY` variable: `echo $DISPLAY`. If unset, set it (e.g., `export DISPLAY=:0`).
- **Tkinter Not Found**:
  - Install Tkinter: `sudo apt-get install python3-tk` (Ubuntu) or equivalent.
- **Other Issues**:
  - Ensure Python 3 is installed and the script is run in a compatible environment.

## Limitations
- Requires a graphical environment; not suitable for terminal-only setups without additional configuration.
- Preserves non-alphabetic characters (e.g., numbers, punctuation) without modification.
- Shift values are normalized (e.g., 27 becomes 1) to stay within the 0-25 range.

## License
This project is provided as-is for educational purposes. Feel free to modify and distribute under the MIT License.

## Contributing
Contributions are welcome! Submit issues or pull requests via GitHub (if hosted) or contact the maintainer for suggestions.