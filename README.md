# CMU Block Dimension Checker

A Python tool to verify whether a given length matches standard **8-inch CMU block dimensions**.  
Supports both **CLI** and **GUI** (Tkinter) modes with smart detection of the best interface.

---

## ✨ Features
- Accepts flexible input formats: `6'4"`, `5-9`, `76`, etc.
- Checks if a dimension is a CMU block size (multiples of 8").
- Shows nearest smaller and larger block dimensions.
- Dual interface:
  - **CLI Mode** (`cli_app.py`)
  - **GUI Mode** (`gui_app.py`)
- Smart entry point (`main.py`) automatically picks CLI or GUI, or use flags `--cli` / `--gui`.

---

## 📂 Project Structure
- `dim_utils.py` – Core logic (parse input, check block sizes, format output).
- `cli_app.py` – Command-line interface.
- `gui_app.py` – Tkinter GUI.
- `main.py` – Entry point and mode selection.

---

## 🚀 Usage

### Run in CLI mode
```bash
python main.py --cli
```

### Run in GUI mode
```bash
python main.py --gui
```

### Example
```bash
Enter a length: 6'4"
✓ 6' 4" is a block dimension.
🡢 Next block dimension: 7' 0"
🡠 Previous block dimension: 5' 8"
```

---

## 📦 Requirements
- Python **3.8+**  
- **Tkinter** (included with most Python installations)  
- **PyInstaller** (only if building executables)

---

## 🛠️ Build & Run (Executable)

### Build GUI version
```bash
pyinstaller main.py --onefile --noconsole --name "Block Dimensions" --icon=".\icon\Icon.ico"
```

### Build CLI version
```bash
pyinstaller main.py --onefile --console --name "Block Dimensions CLI" --icon=".\icon\Icon CLI.ico"
```
