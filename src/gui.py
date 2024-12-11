import tkinter as tk
from tkinter import messagebox
from .cipher_utils import vigenere_encrypt, vigenere_decrypt

class CipherXGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("CipherX - Vigenère Cipher")

        # Frames
        input_frame = tk.Frame(master, padx=10, pady=10)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        control_frame = tk.Frame(master, padx=10, pady=10)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        output_frame = tk.Frame(master, padx=10, pady=10)
        output_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Widgets
        tk.Label(input_frame, text="Input Text:").pack(anchor=tk.W)
        self.input_text = tk.Text(input_frame, height=10)
        self.input_text.pack(fill=tk.BOTH, expand=True)

        tk.Label(control_frame, text="Password:").grid(row=0, column=0, sticky=tk.W)
        self.password_entry = tk.Entry(control_frame, show='*', width=20)
        self.password_entry.grid(row=0, column=1, padx=5)

        self.encrypt_button = tk.Button(control_frame, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.grid(row=0, column=2, padx=5)

        self.decrypt_button = tk.Button(control_frame, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.grid(row=0, column=3, padx=5)

        tk.Label(output_frame, text="Output Text:").pack(anchor=tk.W)
        self.output_text = tk.Text(output_frame, height=10, state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True)

    def encrypt_text(self):
        plaintext = self.input_text.get("1.0", tk.END).strip()
        password = self.password_entry.get().strip()

        if not plaintext or not password:
            messagebox.showwarning("Input Error", "Please provide both text and password.")
            return

        encrypted = vigenere_encrypt(plaintext, password)
        self.display_output(encrypted)

    def decrypt_text(self):
        ciphertext = self.input_text.get("1.0", tk.END).strip()
        password = self.password_entry.get().strip()

        if not ciphertext or not password:
            messagebox.showwarning("Input Error", "Please provide both text and password.")
            return

        decrypted = vigenere_decrypt(ciphertext, password)
        self.display_output(decrypted)

    def display_output(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state=tk.DISABLED)
