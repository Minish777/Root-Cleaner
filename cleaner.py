#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import locale
import argparse
from pathlib import Path
from datetime import datetime

class RootlyCleaner:
    def __init__(self):
        self.version = "3.1-stable"
        self.author = "Rootly"
        self.setup_locale()
        self.colors = self.Colors()
        
        # Основные пути
        self.targets = {
            "User Cache": "~/.cache",
            "System Journal": "/var/log/journal",
            "Thumbnails": "~/.cache/thumbnails",
            "Trash Bin": "~/.local/share/Trash/files",
            "Temp Files": "/tmp",
            "Editor Swap": "~/.local/state/nvim/swap"
        }
        
        # Описания категорий
        self.descriptions = {
            'ru': {
                'User Cache': 'Кэш приложений и браузеров (безопасно)',
                'System Journal': 'Системные логи (очистка через vacuum)',
                'Thumbnails': 'Превью картинок в проводнике',
                'Trash Bin': 'Файлы в вашей корзине',
                'Temp Files': 'Временные данные системы (>24ч)',
                'Editor Swap': 'Временные файлы правки кода'
            },
            'en': {
                'User Cache': 'Application & browser cache (safe)',
                'System Journal': 'System logs (vacuum cleanup)',
                'Thumbnails': 'File manager thumbnails',
                'Trash Bin': 'Files in your system trash',
                'Temp Files': 'Global temporary data (>24h)',
                'Editor Swap': 'Vim/Nvim swap files'
            }
        }

    class Colors:
        CYAN = '\033[96m'
        OK = '\033[92m'
        WARN = '\033[93m'
        FAIL = '\033[91m'
        BLUE = '\033[94m'
        GRAY = '\033[90m'
        END = '\033[0m'
        BOLD = '\033[1m'

    def setup_locale(self):
        try:
            loc = locale.getlocale()[0]
            self.lang = 'ru' if loc and ('ru' in loc.lower()) else 'en'
        except:
            self.lang = 'en'

    def get_ascii(self):
        return f"""{self.colors.CYAN}{self.colors.BOLD}
  ██████╗  ██████╗  ██████╗ ████████╗     ██████╗ 
  ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝    ██╔════╝ 
  ██████╔╝██║   ██║██║   ██║   ██║       ██║      
  ██╔══██╗██║   ██║██║   ██║   ██║       ██║      
  ██║  ██║╚██████╔╝╚██████╔╝   ██║       ╚██████╗ 
  ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝        ╚═════╝{self.colors.END}
          {self.colors.GRAY}v{self.version} | dev by {self.author}{self.colors.END}"""

    def get_size(self, path):
        path = Path(path).expanduser()
        if not path.exists(): return 0
        if path.is_file(): return path.stat().st_size
        return sum(f.stat().st_size for f in path.glob('**/*') if f.is_file())

    def format_size(self, size):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024: return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"

    def rotate_reports(self):
        """Удаляет старые отчеты, оставляя только 5 свежих"""
        reports = sorted(Path('.').glob('report_*.txt'), key=os.path.getmtime)
        while len(reports) > 5:
            reports.pop(0).unlink()

    def run(self, dry_run=True):
        os.system('clear')
        print(self.get_ascii())
        mode = "АНАЛИЗ" if dry_run else "ОЧИСТКА"
        print(f"\n{self.colors.BLUE}╔{"═" * 58}╗{self.colors.END}")
        print(f"{self.colors.BLUE}║{self.colors.BOLD}{mode.center(58)}{self.colors.END}{self.colors.BLUE}║{self.colors.END}")
        print(f"{self.colors.BLUE}╚{"═" * 58}╝{self.colors.END}\n")

        total_bytes = 0
        report_data = []

        for name, p_str in self.targets.items():
            path = Path(p_str).expanduser()
            if not path.exists(): continue

            size = self.get_size(path)
            total_bytes += size
            
            icon = f"{self.colors.WARN}󰔟{self.colors.END}" if dry_run else f"{self.colors.OK}󰄬{self.colors.END}"
            print(f" {icon} {self.colors.BOLD}{name:15}{self.colors.END} │ {self.colors.CYAN}{self.format_size(size):>9}{self.colors.END}")
            print(f"    └─ {self.colors.GRAY}{self.descriptions[self.lang][name]}{self.colors.END}")

            if not dry_run:
                try:
                    if "Journal" in name:
                        os.system("sudo journalctl --vacuum-time=2d > /dev/null 2>&1")
                    else:
                        for item in path.iterdir():
                            if "fontconfig" in str(item): continue
                            report_data.append(str(item))
                            if item.is_file() or item.is_symlink(): item.unlink()
                            elif item.is_dir(): shutil.rmtree(item)
                except: pass

        print(f"\n{self.colors.BLUE}{"─" * 60}{self.colors.END}")
        label = "Будет очищено" if dry_run else "Освобождено"
        print(f" {self.colors.OK}{self.colors.BOLD}{label}: {self.format_size(total_bytes)}{self.colors.END}")
        
        if not dry_run and report_data:
            rep_name = f"report_{datetime.now().strftime('%H%M%S')}.txt"
            with open(rep_name, "w") as f: f.write("\n".join(report_data))
            self.rotate_reports()
            print(f" {self.colors.CYAN}Отчет создан: {rep_name} (старые удалены){self.colors.END}")
        
        input(f"\n{self.colors.GRAY}Enter для возврата...{self.colors.END}")

    def main_menu(self):
        while True:
            try:
                os.system('clear')
                print(self.get_ascii())
                print(f"\n {self.colors.CYAN}1.{self.colors.END} Анализ системы")
                print(f" {self.colors.CYAN}2.{self.colors.END} Запустить очистку")
                print(f" {self.colors.FAIL}q.{self.colors.END} Выход")
                
                choice = input(f"\n {self.colors.BLUE}>>> {self.colors.END}").lower()
                if choice == '1': self.run(dry_run=True)
                elif choice == '2': self.run(dry_run=False)
                elif choice in ['q', 'й', 'exit']: break
            except KeyboardInterrupt:
                print(f"\n\n {self.colors.WARN}Завершение работы...{self.colors.END}")
                break

if __name__ == "__main__":
    app = RootlyCleaner()
    app.main_menu()
