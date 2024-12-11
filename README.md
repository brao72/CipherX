# CipherX

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About The Project

**CipherX** is a minimalist desktop application that allows users to encrypt and decrypt text using the Vigenère cipher. It provides a simple and intuitive graphical user interface (GUI) built with Python’s Tkinter library, making it easy for users to perform encryption and decryption operations with just a few clicks. This project is designed for educational purposes, demonstrating the implementation of classical encryption techniques and GUI development in Python.

## Features

- **Simple Vigenère Cipher Implementation:** Encrypt and decrypt text using the Vigenère cipher algorithm.
- **User-Friendly GUI:** Clean and straightforward interface built with Tkinter.
- **Minimal Input/Output:** Single input area for text, password entry field, and output display.
- **One-Click Operations:** Easily perform encryption and decryption with dedicated buttons.
- **Error Handling:** Informative messages guide users in case of incorrect inputs or errors.
- **Modular Codebase:** Organized code structure separating cipher logic and GUI components.

## Tech Stack

### Frontend

- **Python 3.x:** The primary programming language used for developing the application.
- **Tkinter:** Python's standard GUI library used to create the graphical user interface.

### Backend

- **Vigenère Cipher Algorithm:** Implements the classical Vigenère cipher for text encryption and decryption.
- **Modular Utilities:** Separate modules for cipher logic to ensure clean and maintainable code.
- **Standard Libraries:** Utilizes Python's built-in libraries for string manipulation and file handling.

## Installation

Follow these comprehensive steps to set up the **CipherX** project on your local machine.

### Prerequisites

- **Python 3.x** installed on your system. You can download it from [here](https://www.python.org/downloads/).
- **Git** installed on your system. You can download it from [here](https://git-scm.com/downloads).

### Steps

1. **Clone the Repository**

   Open your terminal and run:

   ```bash
   git clone https://github.com/brao72/CipherX.git

2. **Navigate to the Project Directory**
    
   ```bash
   
   cd CipherX

3. **Verify Installation**
   Ensure that all required files and directories are present. Your project structure should resemble the following:
    
   ```bash
   
   CipherX/
   ├── src/
   │   ├── __init__.py
   │   ├── cipher_utils.py    # Contains Vigenère cipher logic
   │   ├── gui.py             # Contains Tkinter UI code
   │   └── main.py            # Entry point to run the application
   ├── README.md
   ├── requirements.txt      # If any external dependencies (likely none beyond Tkinter)
   └── LICENSE               # MIT License (if desired)

4. **Run the Application**
    
   ```bash
   
   python3 -m src.main

## Usage

Launch the **CipherX** application to start encrypting and decrypting messages.

### How to Use the GUI

1. **Input Text Area:**
   - **Enter Text:** Type or paste the plaintext you wish to encrypt or the ciphertext you wish to decrypt into the "Input Text" area.

2. **Password Entry Field:**
   - **Enter Password:** Type the password that will be used for the Vigenère cipher encryption or decryption. The password is case-insensitive and should consist of alphabetical characters.

3. **Buttons:**
   - **Encrypt:** Click the "Encrypt" button to encrypt the text entered in the "Input Text" area using the provided password. The encrypted text will appear in the "Output Text" area.
   - **Decrypt:** Click the "Decrypt" button to decrypt the text entered in the "Input Text" area using the provided password. The decrypted text will appear in the "Output Text" area.

4. **Output Text Area:**
   - **View Results:** The result of the encryption or decryption operation will be displayed here. You can copy the output by selecting the text and using standard copy commands (e.g., `Ctrl+C` or `Cmd+C`).

### Example Workflow

1. **Encrypting a Message:**
   - **Input:** Enter "hello world" in the "Input Text" area.
   - **Password:** Enter "cipher" in the password field.
   - **Action:** Click "Encrypt".
   - **Output:** The encrypted text appears in the "Output Text" area.

2. **Decrypting a Message:**
   - **Input:** Enter the previously encrypted text in the "Input Text" area.
   - **Password:** Enter "cipher" in the password field.
   - **Action:** Click "Decrypt".
   - **Output:** The original message "hello world" appears in the "Output Text" area.

## Future Enhancements

While the current version of **CipherX** provides fundamental encryption and decryption functionalities, several enhancements can be implemented to improve its features and security:

- **Enhanced Character Support:**
  - Expand the character mapping to include uppercase letters, numbers, and special characters to handle a broader range of inputs.

- **Key Validation:**
  - Implement validation to ensure that the password consists only of alphabetical characters and meets minimum length requirements.

- **Persistent Key Storage:**
  - Allow users to save and load their Vigenère cipher keys securely for future use.

- **GUI Improvements:**
  - Enhance the interface with better layouts, themes, and user experience features such as tooltips and input validation feedback.

- **Logging and Audit Trails:**
  - Implement logging to track encryption and decryption activities for audit purposes or debugging.

- **Support for Multiple Ciphers:**
  - Expand the application to support additional classical ciphers (e.g., Caesar, Substitution) and allow users to select their preferred encryption method.

- **Export/Import Functionality:**
  - Enable users to export encrypted messages to files or import ciphertexts from files for encryption/decryption.

- **Security Enhancements:**
  - Incorporate more secure cryptographic practices, such as handling passwords securely and preventing brute-force attacks.

- **Unit Testing:**
  - Develop comprehensive unit tests to ensure the reliability and correctness of cipher algorithms and GUI functionalities.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html) – Python's standard GUI library.
- [Vigenère Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) – Classical cipher used for encryption and decryption.
- [Python GitHub Templates](https://github.com/github/gitignore) – For creating effective `.gitignore` files.
- [GitHub Guides](https://guides.github.com/) – Comprehensive guides on using Git and GitHub.

   
