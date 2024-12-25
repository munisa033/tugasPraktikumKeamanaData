import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb
import os

def get_image_path():
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
    if img_path:
        return img_path
    else:
        messagebox.showerror("Error", "Path gambar tidak valid.")
        return None

def hide_message():
    image_path = get_image_path()
    if image_path:
        message = entry_message.get()
        if not message:
            messagebox.showerror("Error", "Pesan tidak boleh kosong!")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            try:
                secret = lsb.hide(image_path, message)
                secret.save(save_path)
                messagebox.showinfo("Success", f"Pesan berhasil disembunyikan! Gambar disimpan di: {save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menyimpan gambar: {e}")

def show_message():
    image_path = get_image_path()
    if image_path:
        try:
            clear_message = lsb.reveal(image_path)
            if clear_message:
                entry_result.delete(0, tk.END)
                entry_result.insert(0, clear_message)
            else:
                messagebox.showinfo("No Message", "Tidak ada pesan tersembunyi dalam gambar ini.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menampilkan pesan: {e}")

window = tk.Tk()
window.title("Aplikasi Steganografi")
window.geometry("600x400")
window.configure(bg="#ffe4e1")

title_label = tk.Label(window, text="Aplikasi Steganografi", font=("Helvetica", 18, "bold"), bg="#ffe4e1")
title_label.pack(pady=10)

frame_input = tk.Frame(window, bg="#ffe4e1")
frame_input.pack(pady=10)

label_message = tk.Label(frame_input, text="Masukkan pesan rahasia:", font=("Helvetica", 12), bg="#ffe4e1")
label_message.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_message = tk.Entry(frame_input, width=50, font=("Helvetica", 12))
entry_message.grid(row=0, column=1, padx=10, pady=5)

frame_buttons = tk.Frame(window, bg="#ffe4e1")
frame_buttons.pack(pady=20)

button_hide = tk.Button(frame_buttons, text="Sembunyikan Pesan", font=("Helvetica", 12, "bold"), bg="#ff69b4", fg="white", width=20, command=hide_message)
button_hide.grid(row=0, column=0, padx=10, pady=5)

button_show = tk.Button(frame_buttons, text="Tampilkan Pesan", font=("Helvetica", 12, "bold"), bg="#db7093", fg="white", width=20, command=show_message)
button_show.grid(row=0, column=1, padx=10, pady=5)

frame_output = tk.Frame(window, bg="#ffe4e1")
frame_output.pack(pady=10)

label_result = tk.Label(frame_output, text="Pesan Tersembunyi:", font=("Helvetica", 12), bg="#ffe4e1")
label_result.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_result = tk.Entry(frame_output, width=50, font=("Helvetica", 12))
entry_result.grid(row=0, column=1, padx=10, pady=5)

footer_label = tk.Label(window, text="Dibuat dengan cinta ❤ oleh Anda", font=("Helvetica", 10), bg="#ffe4e1", fg="#555")
footer_label.pack(pady=10)

window.mainloop()
