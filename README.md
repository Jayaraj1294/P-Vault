# P-Vault — Secure Password Manager

P-Vault is a web-based password manager designed to store and manage passwords securely. All passwords are symmetrically encrypted and stored in a database, which is further protected with a hash-encrypted master password.

---

## Features

- **Multiple User Support:**
  - Users can register, log in, and securely manage their own passwords.
  
- **Password Management:**
  - Add, edit, and delete password entries for websites and services.
  
- **Easy Navigation:**
  - Simple, intuitive UI to easily navigate through password vaults.

- **Adaptive Layout:**
  - Responsive design that adapts to any device, ensuring a seamless experience.

- **Password Generator:**
  - Built-in password generator for creating secure and random passwords.

- **Password Strength Checker:**
  - Built-in password Strength Checker for analysing the strength of the passwords.

- **Export Data:**
  - Export password vault entries in CSV or JSON formats for backup or migration.

- **Clipboard Copying:**
  - Copy usernames, passwords, and website URLs to the clipboard with one click.

- **Search:**
  - Search for entries by name for quick access to stored passwords.

- **User Profile Management:**
  - Change a user's name, email, and master password.

- **Account Deletion:**
  - Delete a user’s account along with all its entries permanently.

---

## Tech Stack

- **Frontend:** Bootstrap5 for responsive design and user-friendly interface.
- **Backend:** Flask for the server-side application logic and handling HTTP requests.
- **Database:** MongoDB (for securely storing user data and passwords).
- **Encryption:** AES encryption for password security, with master password hash for authentication.
