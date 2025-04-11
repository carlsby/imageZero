import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from ttkthemes import ThemedTk
from tkinter import ttk
import os

img = None
file_path = None

def select_image():
    global img
    global file_path

    # Öppnar file path
    file_path = filedialog.askopenfilename(title="Välj bild", filetypes=[ 
        ("Tillåtna bildformat", "*.png *.jpg *.jpeg *.bmp *.tiff *.webp"), 
        ("Alla filer", "*.*")
    ])

    if file_path:
        img = Image.open(file_path)
        status_label.config(text=os.path.basename(file_path))

def compress_and_save():
    global img
    global file_path

    if not file_path:
        messagebox.showwarning("Ingen bild", "Välj en bild först")
        return

    # Tar ut storleken på bilden
    myHeight, myWidth = img.size

    # Resizar filen (storlek, KB, MB osv) med hjälp av pillow, detta komprimerar bilden
    img = img.resize((myHeight, myWidth), Image.Resampling.LANCZOS)

    if file_path:
        # Sparar bilden med save path + webp för komprimerade bilder, går även att ändra till jpeg, jpg, png osv
        img.save(file_path+"_zero.webp")
        status_label.config(text=f"Bild sparades till {file_path + '_zero.webp'}")
    else:
        messagebox.showinfo("Misslyckades", "Sparningen misslyckades.")

root = ThemedTk(theme='elegant')  

root.title("ImageZero")
root.geometry("600x400")
root.resizable(False, False)

label = ttk.Label(root, text="ImageZero", font=("Helvetica", 16))
label.pack(pady=10)

select_button = ttk.Button(root, text="Välj bild", command=select_image)
select_button.pack(pady=5)

compress_button = ttk.Button(root, text="Komprimera", command=compress_and_save)
compress_button.pack(pady=5)

status_label = ttk.Label(root, text="", foreground="gray")
status_label.pack(pady=10)

exit_button = ttk.Button(root, text="Avsluta", command=root.destroy)
exit_button.pack(pady=5)

style = ttk.Style()

root.mainloop()
