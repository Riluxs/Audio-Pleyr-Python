# Audio-Player-Python
Audio Player "Rilux-S 2026"

Rilux-S Представляет для вас графический аудио плейр на питон версия 1.0Beta 


# 📥 Инструкция по установке MP3 Player

Пошаговое руководство по установке и настройке MP3 плеера для всех пользователей Linux.

---

## 🐧 Для Ubuntu / Debian / Linux Mint

### Шаг 1: Скачать плеер

**Вариант A: Через браузер**
1. Перейдите на страницу: https://github.com/Riluxs/Audio-Pleyr-Python
2. Нажмите зелёную кнопку **Code** → **Download ZIP**
3. Распакуйте архив в любую папку

**Вариант B: Через терминал (git)**
```bash
# Открыть терминал (Ctrl+Alt+T)
cd ~/Загрузки
git clone https://github.com/Riluxs/Audio-Pleyr-Python.git
cd Audio-Pleyr-Python
```

**Вариант C: Через wget**
```bash
cd ~/Загрузки
wget https://github.com/Riluxs/Audio-Pleyr-Python/archive/refs/heads/main.zip
unzip main.zip
cd Audio-Pleyr-Python-main
```

### Шаг 2: Установить зависимости

Откройте терминал и выполните:

```bash
# Обновить список пакетов
sudo apt update

# Установить Python и Tkinter
sudo apt install python3 python3-tk

# Установить аудио-движок (ffmpeg)
sudo apt install ffmpeg
```

### Шаг 3: Запустить плеер

```bash
# Перейти в папку с плеером
cd ~/Загрузки/Audio-Pleyr-Python

# Запустить
python3 music_rlus.py
```

### Шаг 4: Создать ярлык для запуска (опционально)

Чтобы запускать двойным кликом:

```bash
# Сделать файл исполняемым
chmod +x music_rlus.py

# Настроить файловый менеджер для запуска .py файлов
gsettings set org.gnome.nautilus.preferences executable-text-activation 'launch'
```

Теперь можно запускать двойным кликом по файлу `music_rlus.py`! 🎉

---

## 🎩 Для Fedora / RHEL / CentOS

### Шаг 1: Скачать плеер

```bash
cd ~/Загрузки
git clone https://github.com/Riluxs/Audio-Pleyr-Python.git
cd Audio-Pleyr-Python
```

### Шаг 2: Установить зависимости

```bash
# Установить Python и Tkinter
sudo dnf install python3 python3-tkinter

# Установить ffmpeg
sudo dnf install ffmpeg
```

### Шаг 3: Запустить

```bash
python3 music_rlus.py
```

---

## 🏔️ Для Arch Linux / Manjaro

### Шаг 1: Скачать плеер

```bash
cd ~/Загрузки
wget https://github.com/Rilux-S/mp3-player/archive/refs/heads/main.zip
unzip main.zip
cd mp3-player-main
```

### Шаг 2: Установить зависимости

```bash
# Установить Python, Tkinter и ffmpeg
sudo pacman -S python tk ffmpeg
```

### Шаг 3: Запустить

```bash
python3 mp3_player.py
```

---

## 🎯 Создание иконки в меню приложений

Чтобы плеер появился в меню приложений:

### Шаг 1: Скопировать плеер в удобное место

```bash
# Создать папку для приложения
mkdir -p ~/.local/share/audio-player

# Скопировать туда плеер
cp music_rlus.py ~/.local/share/audio-player/

# Сделать исполняемым
chmod +x ~/.local/share/audio-player/music_rlus.py
```

### Шаг 2: Создать .desktop файл

```bash
nano ~/.local/share/applications/audio-player.desktop
```

Вставьте следующее содержимое:

```ini
[Desktop Entry]
Version=1.0
Type=Application
Name=Audio Player
Comment=Простой аудио плеер
Exec=/home/ВАШ_USERNAME/.local/share/audio-player/music_rlus.py
Icon=multimedia-audio-player
Terminal=false
Categories=AudioVideo;Audio;Player;
Keywords=music;audio;mp3;player;
```

**⚠️ ВАЖНО:** Замените `ВАШ_USERNAME` на ваше имя пользователя!

Узнать имя пользователя:
```bash
echo $USER
```

### Шаг 3: Обновить меню

```bash
# Обновить базу приложений
update-desktop-database ~/.local/share/applications/
```

Готово! Теперь "Audio Player" появится в меню приложений! 🎵

---

## ❓ Решение проблем

### Проблема: "python3: command not found"

**Решение:**
```bash
# Ubuntu/Debian
sudo apt install python3

# Fedora
sudo dnf install python3

# Arch
sudo pacman -S python
```

### Проблема: "No module named 'tkinter'"

**Решение:**
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

### Проблема: "Не найден ни один плеер!"

**Решение:** Установите хотя бы один аудио-движок:

```bash
# Рекомендуется ffmpeg (работает везде)
sudo apt install ffmpeg        # Ubuntu/Debian
sudo dnf install ffmpeg        # Fedora
sudo pacman -S ffmpeg          # Arch

# Или альтернативы
sudo apt install mpg123        # Легковесный MP3 плеер
sudo apt install vlc           # VLC медиаплеер
```

### Проблема: Плеер не запускается двойным кликом

**Решение:**
```bash
# Сделать файл исполняемым
chmod +x music_rlus.py

# Настроить Nautilus для запуска .py файлов
gsettings set org.gnome.nautilus.preferences executable-text-activation 'launch'
```

### Проблема: Не воспроизводится MP3

**Возможные причины:**
1. Не установлен ffmpeg → Установите: `sudo apt install ffmpeg`
2. Файл повреждён → Попробуйте другой MP3 файл
3. Недостаточно прав → Проверьте права на файл: `ls -l файл.mp3`

---

## 🚀 Быстрая установка (одной командой)

### Ubuntu/Debian:
```bash
sudo apt update && sudo apt install -y python3 python3-tk ffmpeg && cd ~/Загрузки && git clone https://github.com/Riluxs/Audio-Pleyr-Python.git && cd Audio-Pleyr-Python && chmod +x music_rlus.py && python3 music_rlus.py
```

### Fedora:
```bash
sudo dnf install -y python3 python3-tkinter ffmpeg && cd ~/Загрузки && git clone https://github.com/Riluxs/Audio-Pleyr-Python.git && cd Audio-Pleyr-Python && chmod +x music_rlus.py && python3 music_rlus.py
```

### Arch:
```bash
sudo pacman -S --noconfirm python tk ffmpeg && cd ~/Загрузки && git clone https://github.com/Riluxs/Audio-Pleyr-Python.git && cd Audio-Pleyr-Python && chmod +x music_rlus.py && python3 music_rlus.py
```

---

## 📞 Нужна помощь?

Если возникли проблемы:
1. Проверьте раздел **"Решение проблем"** выше
2. Откройте Issue на GitHub: https://github.com/Riluxs/Audio-Pleyr-Python/issues
3. Убедитесь, что установлены все зависимости

---

## ✅ Проверка установки

После установки выполните эти команды для проверки:

```bash
# Проверить Python
python3 --version
# Должно показать: Python 3.x.x

# Проверить Tkinter
python3 -c "import tkinter; print('Tkinter OK')"
# Должно показать: Tkinter OK

# Проверить ffmpeg
ffmpeg -version
# Должно показать версию ffmpeg
```

Если все три команды работают - установка прошла успешно! ✅

---

**🎵 Приятного прослушивания музыки!**
