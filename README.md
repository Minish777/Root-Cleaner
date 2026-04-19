# 🚀 Rootly System Cleaner

<p align="center">
  <img src="https://img.shields.io/badge/Version-3.1--stable-cyan?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Platform-Linux-orange?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge" alt="Python">
</p>

---

## 🇷🇺 Описание (RU)

**Rootly System Cleaner** — это мощная, но безопасная утилита для очистки вашей Linux системы. Она создана для тех, кто ценит чистоту диска, но не хочет рисковать стабильностью системы. 

### 🔥 Преимущества
- **Умная фильтрация**: Скрипт никогда не удалит критические файлы, такие как `fontconfig`, чтобы ваши шрифты не «ломались».
- **Авто-ротация отчетов**: Программа хранит только последние 5 логов очистки, автоматически удаляя старые.
- **Безопасность прежде всего**: Очистка системных логов происходит через официальный инструмент `journalctl`.
- **Zero Dependencies**: Работает «из коробки» на любом дистрибутиве с Python 3.

### 🛠️ Инструкция
1. `git clone https://github.com/Minish777/Root-Cleaner.git`
2. `cd root_cleaner`
3. `chmod +x cleaner.py`
4. `./cleaner.py`

---

## 🇺🇸 Description (EN)

**Rootly System Cleaner** is a powerful yet safe utility for cleaning your Linux system. Built for users who value disk space but won't compromise on stability.

### 🔥 Key Features
- **Smart Filtering**: The script never touches critical files like `fontconfig` to prevent font rendering issues.
- **Report Auto-Rotation**: Keeps only the 5 most recent cleanup logs, automatically purging the old ones.
- **Safety First**: System logs are managed via the official `journalctl` vacuum tool.
- **Zero Dependencies**: Runs "out of the box" on any Linux distribution with Python 3.

### 🛠️ Quick Start
1. `git clone https://github.com/Minish777/Root-Cleaner.git`
2. `cd root_cleaner`
3. `chmod +x cleaner.py`
4. `./cleaner.py`

---

## 📂 Targets / Что очищается
| Category | Description | Описание |
| :--- | :--- | :--- |
| **User Cache** | App & browser temporary data | Кэш приложений и браузеров |
| **Journal** | System logs (keeps 2 days) | Системные логи (за 2 дня) |
| **Temp** | Global temporary files (>24h) | Временные файлы системы |
| **Thumbnails** | Image previews | Эскизы изображений |
| **Editor Swap** | Nvim/Vim swap files | Временные файлы редакторов |

---

## 📝 License / Лицензия
This project is licensed under the **MIT License**.

## 🤝 Support
If you liked this project, feel free to give it a ⭐!
*Developed by **Rootly**. Ty for download!*
