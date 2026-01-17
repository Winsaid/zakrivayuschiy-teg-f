#!/usr/bin/env python3
"""
Простой HTTP сервер для запуска статического сайта на localhost.
Использование: python server.py
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 8000
HOST = "localhost"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    # Переходим в директорию скрипта
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Создаем сервер
    with socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler) as httpd:
        url = f"http://{HOST}:{PORT}"
        print(f"Сервер запущен на {url}")
        print(f"Откройте браузер и перейдите по адресу: {url}")
        print("Для остановки сервера нажмите Ctrl+C")
        
        # Автоматически открываем браузер
        try:
            webbrowser.open(url)
        except Exception:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер остановлен")

if __name__ == "__main__":
    main()

