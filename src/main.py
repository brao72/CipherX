import tkinter as tk
from .gui import CipherXGUI

def main():
    root = tk.Tk()
    app = CipherXGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
