# AccessProjects - Mac Menu Bar App (Open Projects in Visual Studio Code)

AccessProjects is a lightweight macOS menu bar application that helps you quickly access your most recent coding projects.  
It displays your 3 most recently updated project folders and opens them directly in **Visual Studio Code** with a single click.

Built with Python using the `rumps` library for native Mac menu bar apps.

---
## ✅ Features
- 🧠 Automatically detects and lists your 3 most recently updated project folders.
- ⚡ Clicking a project **instantly opens it in Visual Studio Code**.
- ➕ Dynamically add new folders at runtime (no code editing required).
- 🔥 Lightweight, responsive, and simple to run.
- 🖥️ Built entirely with Python for macOS environments.

---
## 🚀 How to Set Up and Use
### 1. Install the required Python package
```bash
pip3 install rumps
```
✅ Done once.

---
### 2. Make sure the `code` command is available (required!)
1. Open **Visual Studio Code**.
2. Press **Cmd + Shift + P**.
3. Type: `Shell Command: Install 'code' command in PATH`
4. Click it.

✅ This runs:
```bash
ln -s /Applications/Visual\ Studio\ Code.app/Contents/Resources/app/bin/code /usr/local/bin/code
```

Without this, clicking projects won't open VS Code.

---
### 3. (Optional) Customize your starting folders
Inside `main.py`, update:
```python
search_directories = [
    "/Users/yourusername/PycharmProjects",
    "/Users/yourusername/Java_Projects"
]
```
Replace with any folder paths you want.

---
### 4. Run the application
```bash
cd /path/to/AccessProjects
python3 main.py
```

✅ "Access" appears in your macOS menu bar.

---
### 5. Using the App
- Click "Access" in the menu bar.
- See your most recent projects.
- Click to open in VS Code.
- Use "Add Folder" to dynamically add new project directories at runtime.

✅ No restart needed.

---
## 🛠️ Requirements
| Item | Requirement |
|:-----|:-------------|
| OS | macOS |
| Python | 3.6+ |
| VS Code | Installed |
| rumps | Installed via pip |
| code command | Installed via Shell Command in VS Code |

---
## 📦 Folder Structure
```
AccessProjects/
├── accessProjects.py
├── main.py
└── README.md
```

---
# 🎯 Quick Setup Summary
```bash
pip3 install rumps
# Install 'code' command inside VS Code
cd /path/to/AccessProjects
python3 main.py
```