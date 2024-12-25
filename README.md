
# 🖱️ Auto Clicker Program

A customizable Python program that automates mouse clicks at specified coordinates. 🚀  
This project includes a **configuration mode** to dynamically add, edit, and reset click coordinates. Perfect for repetitive tasks! 🌟

---

## ✨ Features

- **Automated Mouse Clicking** 🖱️  
  Perform clicks on predefined coordinates at regular intervals.

- **Configuration Mode** 🛠️  
  Add new coordinates dynamically by clicking on the screen.

- **Reset Coordinates** 🔄  
  Clear all saved coordinates with a single key.

- **Keyboard Controls** ⌨️  
  Control the program's behavior with simple keyboard shortcuts.

---

## 🔧 Setup

### Prerequisites
Make sure you have Python installed on your system.  
Install the required libraries using:
```bash
pip install -r requirements.txt
```

### How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/alekxays/auto-clicker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd autoclicker
   ```
3. Run the program:
   ```bash
   python main.py
   ```

---

## 🎮 Keyboard Controls

| Key   | Action                                |
|-------|---------------------------------------|
| `s`   | Start the auto-clicking program       |
| `p`   | Pause the auto-clicking program       |
| `c`   | Enable/disable configuration mode     |
| `r`   | Reset all saved coordinates           |
| `q`   | Quit the program                      |

### 🛠️ Configuration Mode
When configuration mode (`c`) is active:
- Each mouse click saves the coordinates of the click location.
- Multiple clicks are added to the list.
- Press `c` again to exit configuration mode.

---

## 🚀 Example Usage

1. Start the program with `python main.py`.
2. Press `c` to enable configuration mode and click on the screen to save coordinates.
3. Press `s` to start clicking at the saved coordinates.
4. Use `p` to pause or `r` to reset the list of coordinates.
5. Press `q` to quit the program.

---

## 🛡️ Dependencies

The project uses the following Python libraries:
- `pyautogui` 🖱️
- `pynput` ⌨️

Install them with:
```bash
pip install pyautogui pynput
```

---

## 💡 Future Improvements
- Add a graphical user interface (GUI) for easier configuration 🎨
- Support saving and loading coordinate configurations 🗂️
- Add a randomized delay for clicks ⏱️

---

## 🧑‍💻 Contributing

Contributions are welcome! 🎉  
Feel free to fork the repository, create a feature branch, and submit a pull request. 🛠️

---

## 📜 License

This project is licensed under the MIT License. 📄  
Feel free to use and modify it as you like.

---

### 📧 Contact

For questions or feedback, reach out to **[hey@alexandreboissel.me](mailto:hey@alexandreboissel.me)**.

Happy clicking! ✨
