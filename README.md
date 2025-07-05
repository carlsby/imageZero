<h1>
  ImageZero
</h1>

**ImageZero** is a minimal image compression tool built in Python using **Tkinter** and **Pillow**.  
It lets you quickly select and compress images into efficient `.webp` files with a simple GUI.

---

## 🖼️ Features

- 🧠 Simple and intuitive interface
- 💾 Compresses common image formats (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`, `.webp`)
- ⚡ Uses high-quality Lanczos resampling for resizing
- 📁 Saves compressed images in `.webp` format
- 🎨 Uses `ttkthemes` for a modern themed UI

---

## 🧰 Requirements

- Python 3.8+
- [Pillow](https://pypi.org/project/Pillow/)
- [ttkthemes](https://pypi.org/project/ttkthemes/)

Install dependencies:

```bash
pip install pillow ttkthemes
```

## 🚀 Usage
#### 1. Run the application:
```bash
python imagezero.py
```
#### 2. Click “Välj bild” to select an image.
#### 3. Click “Komprimera” to compress and save the image as a .webp file.
#### 4. The app will save the compressed image to the same location with _zero.webp added to the filename.
