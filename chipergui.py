import tkinter as tk
from tkinter import messagebox

def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def encrypt_text():
    plain_text = entry_plain_text.get()
    shift = shift_value.get()
    try:
        shift = int(shift)
        cipher_text = enkripsi(plain_text, shift)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, cipher_text)
    except ValueError:
        messagebox.showerror("Error", "Pergeseran harus berupa angka")

def decrypt_text():
    cipher_text = entry_plain_text.get()
    shift = shift_value.get()
    try:
        shift = int(shift)
        plain_text = dekripsi(cipher_text, shift)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, plain_text)
    except ValueError:
        messagebox.showerror("Error", "Pergeseran harus berupa angka")

# Setup GUI
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("600x400")
window.configure(bg="#ffe4e1")

# Title label
title_label = tk.Label(window, text="Aplikasi Caesar Cipher", font=("Helvetica", 18, "bold"), bg="#ffe4e1")
title_label.pack(pady=10)

# Plain text input
frame_input = tk.Frame(window, bg="#ffe4e1")
frame_input.pack(pady=10)

label_plain_text = tk.Label(frame_input, text="Masukkan teks:", font=("Helvetica", 12), bg="#ffe4e1")
label_plain_text.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_plain_text = tk.Entry(frame_input, width=50, font=("Helvetica", 12))
entry_plain_text.grid(row=0, column=1, padx=10, pady=5)

# Shift input
label_shift = tk.Label(frame_input, text="Masukkan nilai pergeseran:", font=("Helvetica", 12), bg="#ffe4e1")
label_shift.grid(row=1, column=0, padx=10, pady=5, sticky="w")
shift_value = tk.Entry(frame_input, width=10, font=("Helvetica", 12))
shift_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Buttons for encryption and decryption
frame_buttons = tk.Frame(window, bg="#ffe4e1")
frame_buttons.pack(pady=20)

button_encrypt = tk.Button(frame_buttons, text="Enkripsi", font=("Helvetica", 12, "bold"), bg="#ff69b4", fg="white", width=15, command=encrypt_text)
button_encrypt.grid(row=0, column=0, padx=10, pady=5)

button_decrypt = tk.Button(frame_buttons, text="Dekripsi", font=("Helvetica", 12, "bold"), bg="#db7093", fg="white", width=15, command=decrypt_text)
button_decrypt.grid(row=0, column=1, padx=10, pady=5)

# Result output
frame_output = tk.Frame(window, bg="#ffe4e1")
frame_output.pack(pady=10)

label_result = tk.Label(frame_output, text="Hasil:", font=("Helvetica", 12), bg="#ffe4e1")
label_result.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_result = tk.Entry(frame_output, width=50, font=("Helvetica", 12))
entry_result.grid(row=0, column=1, padx=10, pady=5)

# Footer
footer_label = tk.Label(window, text="Dibuat dengan cinta ❤ oleh Anda", font=("Helvetica", 10), bg="#ffe4e1", fg="#555")
footer_label.pack(pady=10)

# Run the application
window.mainloop()
