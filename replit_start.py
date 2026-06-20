import subprocess
import threading
import os
import sys
import time
import http.server
import socketserver

PORT = int(os.environ.get('PORT', 5001))

def run_bot():
    """Run the Discord bot"""
    print("[STARTUP] Starting Discord bot...")
    try:
        subprocess.run([sys.executable, "-u", "main.py"], check=False)
    except Exception as e:
        print(f"[ERROR] Bot crashed: {e}")

def run_dashboard():
    """Run the Flask dashboard"""
    print("[STARTUP] Starting Dashboard...")
    try:
        subprocess.run([
            sys.executable, "-u", "-m", "gunicorn", "app:app",
            "--bind", f"0.0.0.0:{PORT}",
            "--timeout", "120"
        ], check=False)
    except Exception as e:
        print(f"[ERROR] Dashboard crashed: {e}")

def keep_alive():
    """Simple HTTP server to keep Replit alive"""
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("0.0.0.0", PORT + 1), Handler) as httpd:
        print(f"[KEEPALIVE] Server running on port {PORT + 1}")
        httpd.serve_forever()

if __name__ == "__main__":
    print("=" * 50)
    print("  MAX BOT - Starting on Replit...")
    print("=" * 50)
    
    # Start keep-alive server in a thread
    alive_thread = threading.Thread(target=keep_alive, daemon=True)
    alive_thread.start()
    
    # Start bot in a thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Start dashboard in main thread
    run_dashboard()
