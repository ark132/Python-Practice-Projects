# 🖥️ CLI File Manager (v0.1) — Pure Python + SQLite3

Welcome to **Day 2** of my daily GitHub commit journey! 🚀

## 📝 Today's Story

Ngl, I hit this one close to the wire — committed at **11 PM on 31st**, and honestly there was a moment I thought I wasn't going to make it today. But with consistent effort (and a little help from VS Code's built-in AI when I got stuck), I pulled it off. 💪

Today I started building **v0.1** of an upcoming project — a stepping stone toward something bigger I have planned. This is a **CLI File Manager**, built with pure Python and the `sqlite3` module.

## 🛠️ What it does

The project uses a database (`cli.db`) to store CRUD info about files, and is structured around 5 core functions + a `main()`:

- **`list_Files()`** — loops through all stored rows using `cursor.fetchall()` in a simple `for` loop
- **`create_Files()`** — opens a new file in write mode (in `main()`), then extracts and stores its `name`, `path`, and `file_type` using `os`-related parameters
- **`read_Files()`** — opens an existing file in read mode (in `main()`), extracting the same `name`, `path`, `file_type` details
- **`update_Files()`** — uses `os.rename(old_name, new_name)` to rename the file on disk, then updates both old and new file details (`name`, `path`, `type`) in the database
- **`delete_Files()`** — uses `os.remove()` to delete the file from disk, then removes its matching `name` and `path` from the database (no need to track extension here)

### 📦 Key `os` parameters used throughout:
```python
name = os.path.basename(File_name)
path = os.path.abspath(File_name)
file_type = os.path.splitext(File_name)[1]
```

## 🧩 Core concepts practiced
- File Handling
- Exception Handling
- SQLite (CRUD operations)
- The `os` module for interacting with the operating system

## 🐞 Errors today
Ran into a good number of **syntax-related errors** along the way — didn't note every single one down in the moment, but each one forced a closer look at the code and helped it click a bit more. Lesson for tomorrow: jot bugs down *as they happen*, not after. 📝

---
⭐ *One error at a time, one commit at a day, one skill leveled up.*