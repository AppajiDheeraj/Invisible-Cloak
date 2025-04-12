# Invisible-Cloak

# 🧙‍♂️ Invisibility Cloak using OpenCV (Harry Potter Style)

A fun computer vision project that lets you disappear in real-time using an invisibility cloak effect! Built with Python and OpenCV, this script replaces the cloak area with a captured background, creating the illusion of invisibility.
---

## 🎥 Demo

![Demo](invisiblecloak-ezgif.com-optimize.gif)

---

## 🚀 Features

- 🔍 Real-time cloak detection
- 🟥 Supports red and green cloak colors
- 🎯 Customizable color detection via HSV masking
- 💫 Morphological operations for smooth masking
- 🎥 Works with your webcam

---

## 🧰 Tech Stack

- Python
- OpenCV
- NumPy

---

## 📁 Project Structure <br>

invisibility_cloak/ <br>
├── invisibility_cloak.py # Main script <br>
├── README.md # Project description <br>

---

## 🛠️ How It Works <br>

1. Captures the **background** for the first 60 frames <br>
2. Detects a specific **cloak color** (default is red) <br>
3. Masks the cloak area using **HSV color space** <br>
4. Applies **morphological filtering** to clean the mask <br>
5. Overlays the **captured background** in place of the cloak <br>
6. Produces a final output where the cloak appears invisible! <br>

---

## ⚙️ Configuration <br>

You can change the cloak color by editing the `cloak_color` variable: <br>

```python
cloak_color = "red"  # or "green"
```
---

## 🧪 HSV Color Range for Cloak Detection

| Color | HSV Lower Range                     | HSV Upper Range                     |
|-------|-------------------------------------|-------------------------------------|
| Red   | [0, 120, 70] and [170, 120, 70]     | [10, 255, 255] and [180, 255, 255]  |
| Green | [50, 80, 50]                        | [90, 255, 255]                      |

---

## 🧽 Morphological Operations Used

| Operation | Kernel Size | Purpose             |
|----------|-------------|---------------------|
| Close    | (7, 7)       | Fill small holes    |
| Open     | (5, 5)       | Remove noise        |
| Dilation | (10, 10)     | Strengthen mask     |

---

## 🕹️ How to Run<br>
1. Clone the repository<br>
```bash
git clone https://github.com/your-username/invisibility-cloak
cd invisibility-cloak
```
<br>
2. Install dependencies<br>

```bash
pip install opencv-python numpy
```
<br>
3. Run the script<br>

```bash
python invisibility_cloak.py
```
<br>
Make sure you're wearing a red or green cloak and that your background is relatively static.

---

## 🧹 Clean Exit<br>
Press ESC to close the window and stop the program.<br>

---

Made with 💻 and 🪄 by AppajiDheeraj
