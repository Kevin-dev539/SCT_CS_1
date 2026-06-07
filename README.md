# Caesar Cipher Encryption and Decryption Tool

## Overview

This project is a Python-based implementation of the Caesar Cipher, one of the oldest and simplest encryption techniques in cryptography. The program allows users to encrypt and decrypt messages by specifying a shift value (key).

The project demonstrates fundamental concepts of cryptography, string manipulation, and user interaction in Python.

---

## Features

* Encrypt plaintext messages using a custom shift key.
* Decrypt ciphertext messages using the correct shift key.
* Supports both uppercase and lowercase letters.
* Preserves spaces, numbers, and special characters.
* Interactive menu-driven interface.
* Simple and beginner-friendly implementation.

---

## How the Caesar Cipher Works

The Caesar Cipher is a substitution cipher in which each letter of the plaintext is shifted by a fixed number of positions in the alphabet.

### Example

Plaintext:
HELLO

Shift Value:
3

Ciphertext:
KHOOR

Each character is shifted three positions forward in the alphabet:

H → K

E → H

L → O

L → O

O → R

To decrypt the message, the same shift value is applied in the opposite direction.

---

## Concepts Used

### Python Fundamentals

* Variables
* Data Types
* Functions
* Loops
* Conditional Statements
* User Input Handling

### String Processing

* Character iteration
* String concatenation
* Alphabet validation using `isalpha()`

### ASCII Character Manipulation

* `ord()` function
* `chr()` function

### Mathematical Concepts

* Modular Arithmetic (`% 26`)
* Character shifting

### Cryptography Concepts

* Encryption
* Decryption
* Symmetric Key Cryptography
* Classical Cryptographic Algorithms

---
## Program Flow
1. Display menu options.
2. Accept user choice.
3. Input message and shift value.
4. Perform encryption or decryption.
5. Display the result.
6. Repeat until the user exits the program.
--
## Limitations
* The Caesar Cipher is not secure for modern applications.
* The encrypted message does not store the shift key.
* Decryption requires knowledge of the original shift value.
* The cipher can be easily broken using brute-force attacks due to the limited number of possible keys.

---
## Learning Outcomes
Through this project, I gained practical experience in:
* Implementing classical encryption techniques.
* Working with character encoding and ASCII values.
* Applying mathematical operations in programming.
* Developing interactive Python applications.
* Understanding the fundamentals of cryptography and cybersecurity.
--
## Future Improvements
* Add a brute-force attack mode for unknown keys.
* Store encryption keys securely.
* Implement more advanced encryption algorithms.
* Create a graphical user interface (GUI).
* Add file encryption and decryption support.
---
## Author
Developed as a learning project to explore Python programming and the fundamentals of cryptography.
