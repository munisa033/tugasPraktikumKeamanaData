import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt():
    plain_text = plain_text_entry.get()
    key = key_entry.get()
    if len(key) != 8:
        messagebox.showerror("Error", "Kunci harus terdiri dari 8 karakter.")
        return
    try:
        des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
        encrypted_text = des.encrypt(padded_text)
        encoded_text = base64.b64encode(encrypted_text).decode('utf-8')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, encoded_text)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def decrypt():
    encrypted_text = plain_text_entry.get()
    key = key_entry.get()
    if len(key) != 8:
        messagebox.showerror("Error", "Kunci harus terdiri dari 8 karakter.")
        return
    try:
        des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
        decoded_text = base64.b64decode(encrypted_text)
        decrypted_text = unpad(des.decrypt(decoded_text), DES.block_size).decode('utf-8')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, decrypted_text)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Setup GUI
window = tk.Tk()
window.title("Aplikasi DES")
window.geometry("700x500")
window.configure(bg="#ffe4e1")

# Title label
title_label = tk.Label(window, text="Aplikasi DES Encryption/Decryption", font=("Helvetica", 18, "bold"), bg="#ffe4e1")
title_label.pack(pady=10)

# Plain Text Input
frame_plain = tk.Frame(window, bg="#ffe4e1")
frame_plain.pack(pady=10)

plain_text_label = tk.Label(frame_plain, text="Teks Asli/Enkripsi:", font=("Helvetica", 12), bg="#ffe4e1")
plain_text_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
plain_text_entry = tk.Entry(frame_plain, width=50, font=("Helvetica", 12))
plain_text_entry.grid(row=0, column=1, padx=10, pady=5)

# Key Input
frame_key = tk.Frame(window, bg="#ffe4e1")
frame_key.pack(pady=10)

key_label = tk.Label(frame_key, text="Kunci (8 karakter):", font=("Helvetica", 12), bg="#ffe4e1")
key_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
key_entry = tk.Entry(frame_key, width=50, font=("Helvetica", 12))
key_entry.grid(row=0, column=1, padx=10, pady=5)

# Buttons for Encryption and Decryption
frame_buttons = tk.Frame(window, bg="#ffe4e1")
frame_buttons.pack(pady=20)

button_encrypt = tk.Button(frame_buttons, text="Enkripsi", font=("Helvetica", 12, "bold"), bg="#ff69b4", fg="white", width=20, command=encrypt)
button_encrypt.grid(row=0, column=0, padx=10, pady=5)

button_decrypt = tk.Button(frame_buttons, text="Dekripsi", font=("Helvetica", 12, "bold"), bg="#db7093", fg="white", width=20, command=decrypt)
button_decrypt.grid(row=0, column=1, padx=10, pady=5)

# Result Output
frame_output = tk.Frame(window, bg="#ffe4e1")
frame_output.pack(pady=10)

result_label = tk.Label(frame_output, text="Hasil:", font=("Helvetica", 12), bg="#ffe4e1")
result_label.grid(row=0, column=0, padx=10, pady=5, sticky="nw")
result_text = tk.Text(frame_output, width=50, height=10, font=("Helvetica", 12))
result_text.grid(row=0, column=1, padx=10, pady=5)

# Footer
footer_label = tk.Label(window, text="Dibuat dengan cinta ❤ oleh Anda", font=("Helvetica", 10), bg="#ffe4e1", fg="#555")
footer_label.pack(pady=10)

# Run the application
window.mainloop()
