#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Простой MP3 плеер для Ubuntu
Запуск: python3 mp3_player.py
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import threading

class MP3Player:
    def __init__(self, root):
        self.root = root
        self.root.title("Rliux-S 1.0beta")
        self.root.geometry("500x400")
        self.root.configure(bg='#2c3e50')
        
        self.current_file = None
        self.process = None
        self.is_playing = False
        
        self.setup_ui()
        
    def setup_ui(self):
        title_label = tk.Label(
            self.root, 
            text="Rilux-S Audio Pleyr", 
            font=("Arial", 24, "bold"),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=20)
        
        
        self.file_label = tk.Label(
            self.root,
            text="Файл не выбран",
            font=("Arial", 12),
            bg='#34495e',
            fg='#ecf0f1',
            wraplength=450,
            height=3
        )
        self.file_label.pack(pady=10, padx=20, fill='x')
        
        
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(pady=20)
        
        
        self.select_btn = tk.Button(
            button_frame,
            text="📁 Выбрать MP3",
            command=self.select_file,
            font=("Arial", 12, "bold"),
            bg='#3498db',
            fg='white',
            width=15,
            height=2,
            cursor='hand2'
        )
        self.select_btn.grid(row=0, column=0, padx=10)
        
        # Кнопка воспроизведения
        self.play_btn = tk.Button(
            button_frame,
            text="▶️ Играть",
            command=self.play,
            font=("Arial", 12, "bold"),
            bg='#27ae60',
            fg='white',
            width=15,
            height=2,
            cursor='hand2',
            state='disabled'
        )
        self.play_btn.grid(row=0, column=1, padx=10)
        
        
        self.stop_btn = tk.Button(
            button_frame,
            text="⏹️ Стоп",
            command=self.stop,
            font=("Arial", 12, "bold"),
            bg='#e74c3c',
            fg='white',
            width=15,
            height=2,
            cursor='hand2',
            state='disabled'
        )
        self.stop_btn.grid(row=1, column=0, columnspan=2, pady=10)
        
        
        self.status_label = tk.Label(
            self.root,
            text="Статус: Ожидание",
            font=("Arial", 10),
            bg='#2c3e50',
            fg='#95a5a6'
        )
        self.status_label.pack(pady=10)
        
    
        info_text = "Rilux-S 2026"
        info_label = tk.Label(
            self.root,
            text=info_text,
            font=("Arial", 9),
            bg='#2c3e50',
            fg='#7f8c8d'
        )
        info_label.pack(pady=5)
        
    def select_file(self):
        """Выбор MP3 файла"""
        filename = filedialog.askopenfilename(
            title="Выберите MP3 файл",
            filetypes=[
                ("MP3 файлы", "*.mp3"),
                ("Все аудио", "*.mp3 *.wav *.ogg *.flac"),
                ("Все файлы", "*.*")
            ]
        )
        
        if filename:
            self.current_file = filename
            file_name = os.path.basename(filename)
            self.file_label.config(text=f"📀 {file_name}")
            self.play_btn.config(state='normal')
            self.status_label.config(text="Статус: Готов к воспроизведению")
    
    def play(self):
        """Воспроизведение MP3"""
        if not self.current_file:
            messagebox.showwarning("Предупреждение", "Сначала выберите файл!")
            return
        
        if self.is_playing:
            messagebox.showinfo("Инфо", "Уже играет!")
            return
        
    
        self.stop()
        
        
        players = [
            ['ffplay', '-nodisp', '-autoexit', self.current_file],
            ['mpg123', self.current_file],
            ['cvlc', '--play-and-exit', self.current_file],
            ['mplayer', self.current_file]
        ]
        
        success = False
        for player_cmd in players:
            try:
                self.process = subprocess.Popen(
                    player_cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                success = True
                break
            except FileNotFoundError:
                continue
        
        if not success:
            messagebox.showerror(
                "Ошибка",
                "Не найден ни один плеер!\n\n"
                "Установите один из:\n"
                "sudo apt install ffmpeg\n"
                "sudo apt install mpg123\n"
                "sudo apt install vlc"
            )
            return
        
        self.is_playing = True
        self.play_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        self.status_label.config(text="Статус: ▶️ Воспроизведение...")

        
        threading.Thread(target=self.monitor_playback, daemon=True).start()
    
    def monitor_playback(self):
        """Отслеживание окончания воспроизведения"""
        if self.process:
            self.process.wait()
            self.is_playing = False
            self.root.after(0, self.playback_finished)
    
    def playback_finished(self):
        """Колбэк после окончания воспроизведения"""
        self.play_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.status_label.config(text="Статус: Воспроизведение завершено")
    
    def stop(self):
        """Остановка воспроизведения"""
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=2)
            except:
                try:
                    self.process.kill()
                except:
                    pass
            self.process = None
        
        self.is_playing = False
        self.play_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.status_label.config(text="Статус: Остановлено")

def main():
    root = tk.Tk()
    app = MP3Player(root)
    root.mainloop()

if __name__ == "__main__":
    main()
