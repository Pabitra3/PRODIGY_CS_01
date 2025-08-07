import tkinter as tk
from tkinter import messagebox, ttk

class CaesarCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        # Center the window
        self.root.eval('tk::PlaceWindow . center')

        # Styling
        self.root.configure(bg="#f0f0f0")
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
        style.configure("TButton", font=("Helvetica", 10))
        style.configure("TRadiobutton", font=("Helvetica", 10), background="#f0f0f0")

        # Main Frame
        frame = ttk.Frame(root, padding="10")
        frame.grid(row=0, column=0, sticky="nsew")
        frame.configure(style="TFrame")

        # Labels and Entries
        ttk.Label(frame, text="Message:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.message_entry = ttk.Entry(frame, width=30, font=("Helvetica", 10))
        self.message_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Shift Value:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.shift_entry = ttk.Entry(frame, width=10, font=("Helvetica", 10))
        self.shift_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Radio Buttons for Encrypt/Decrypt
        self.mode = tk.StringVar(value="encrypt")
        ttk.Radiobutton(frame, text="Encrypt", variable=self.mode, value="encrypt").grid(row=2, column=0, padx=5, pady=5)
        ttk.Radiobutton(frame, text="Decrypt", variable=self.mode, value="decrypt").grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        ttk.Button(frame, text="Process", command=self.process).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="Clear", command=self.clear).grid(row=4, column=0, pady=5)
        ttk.Button(frame, text="Exit", command=self.exit).grid(row=4, column=1, pady=5)

        # Result Display
        ttk.Label(frame, text="Result:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.result_text = tk.Text(frame, height=4, width=30, font=("Helvetica", 10), bg="#ffffff")
        self.result_text.grid(row=5, column=1, padx=5, pady=5)
        self.result_text.config(state="disabled")

    def caesar_encrypt(self, text, shift):
        if not text:
            return "Error: Empty message provided"
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_base = 65 if char.isupper() else 97
                shifted = (ord(char) - ascii_base + shift) % 26 + ascii_base
                encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        return encrypted_text

    def caesar_decrypt(self, text, shift):
        return self.caesar_encrypt(text, -shift)

    def process(self):
        message = self.message_entry.get().strip()
        shift_text = self.shift_entry.get().strip()

        # Reset entry field colors
        self.message_entry.configure(style="TEntry")
        self.shift_entry.configure(style="TEntry")

        if not message:
            self.message_entry.configure(style="Error.TEntry")
            messagebox.showerror("Error", "Message cannot be empty!")
            return

        try:
            shift = int(shift_text)
            shift = shift % 26 if shift >= 0 else (shift % 26)
        except ValueError:
            self.shift_entry.configure(style="Error.TEntry")
            messagebox.showerror("Error", "Please enter a valid number for shift value!")
            return

        if self.mode.get() == "encrypt":
            result = self.caesar_encrypt(message, shift)
        else:
            result = self.caesar_decrypt(message, shift)

        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state="disabled")

    def clear(self):
        self.message_entry.delete(0, tk.END)
        self.shift_entry.delete(0, tk.END)
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state="disabled")
        self.mode.set("encrypt")
        self.message_entry.configure(style="TEntry")
        self.shift_entry.configure(style="TEntry")

    def exit(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    # Configure error entry style
    style = ttk.Style()
    style.configure("Error.TEntry", fieldbackground="#ffcccc")
    app = CaesarCipherGUI(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("Goodbye!")
        root.destroy()

if __name__ == "__main__":
    main()