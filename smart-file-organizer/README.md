# 📁 Smart File Organizer CLI

A simple and powerful Python CLI tool that automatically organizes files in a folder into categorized subfolders like Images, Documents, Videos, and more.

---

## 🚀 Features

* 📂 Automatic file categorization based on extensions
* 🔁 Handles duplicate file names intelligently
* 🧾 Maintains a log file for all operations
* ⚡ Fast and lightweight (no external dependencies)
* 💻 Beginner-friendly and easy to use

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/smart-file-organizer.git
```

2. Navigate to the project folder:

```bash
cd smart-file-organizer
```

3. Run the script:

```bash
python main.py
```

---

## ▶️ Usage

1. Run the program
2. Enter the folder path you want to organize
3. Confirm the action
4. Done! Files will be sorted automatically

Example:

```bash
Enter folder path to organize: C:/Users/YourName/Downloads
Organize files? (y/n): y
```

---

## 📂 File Categories

The tool organizes files into the following folders:

* 🖼️ Images → `.jpg`, `.png`, `.jpeg`, `.gif`, `.bmp`
* 📄 Documents → `.pdf`, `.docx`, `.txt`, `.xlsx`
* 🎥 Videos → `.mp4`, `.mkv`, `.avi`, `.mov`
* 🎵 Audio → `.mp3`, `.wav`, `.aac`
* 📦 Archives → `.zip`, `.rar`, `.tar`, `.gz`
* 💻 Scripts → `.py`, `.js`, `.html`, `.css`
* 📁 Others → Unknown file types

---

## 📝 Log File

All actions are recorded in:

```
organizer.log
```

Example log:

```
2026-04-11 10:30:12 - Moved file.jpg → Images/
```

---

## 📁 Project Structure

```
smart-file-organizer/
│── main.py
│── README.md
│── organizer.log (auto-generated)
```

---

## 💡 Future Improvements

* 🖥️ GUI version (Tkinter / PyQt)
* 🧠 AI-based smart categorization
* ⚙️ Custom user-defined rules
* 🔄 Automatic background monitoring

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

Built using Python standard libraries:

* `os`
* `shutil`
* `datetime`

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

Made with ❤️ by Jagrut
